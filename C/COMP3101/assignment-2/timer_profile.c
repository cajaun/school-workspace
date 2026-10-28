#define _DEFAULT_SOURCE
#define _POSIX_C_SOURCE 200809L

#include "timer_profile.h"

#include <errno.h>
#include <signal.h>
#include <stdio.h>
#include <sys/time.h>

#define TIMER_INTERVAL_SECONDS 1
#define MICROSECONDS_PER_SECOND 1000000LL

static volatile sig_atomic_t wall_ticks;
static volatile sig_atomic_t user_ticks;
static volatile sig_atomic_t total_cpu_ticks;

static void handle_wall_timer(int signal_number)
{
    (void)signal_number;
    wall_ticks++;
}

static void handle_user_timer(int signal_number)
{
    (void)signal_number;
    user_ticks++;
}

static void handle_total_cpu_timer(int signal_number)
{
    (void)signal_number;
    total_cpu_ticks++;
}

static int create_timer_signal_set(sigset_t *set)
{
    if (sigemptyset(set) == -1) {
        return -1;
    }

    if (sigaddset(set, SIGALRM) == -1 ||
        sigaddset(set, SIGVTALRM) == -1 ||
        sigaddset(set, SIGPROF) == -1) {
        return -1;
    }

    return 0;
}

static int install_handler(int signal_number, void (*handler)(int))
{
    struct sigaction action = {0};

    if (sigemptyset(&action.sa_mask) == -1) {
        return -1;
    }

    action.sa_handler = handler;
    action.sa_flags = SA_RESTART;

    return sigaction(signal_number, &action, 0);
}

static int arm_timer(int timer_type)
{
    struct itimerval timer = {0};

    timer.it_value.tv_sec = TIMER_INTERVAL_SECONDS;
    timer.it_interval.tv_sec = TIMER_INTERVAL_SECONDS;

    return setitimer(timer_type, &timer, 0);
}

static int disarm_timer(int timer_type)
{
    struct itimerval timer = {0};

    return setitimer(timer_type, &timer, 0);
}

static long long elapsed_microseconds(sig_atomic_t ticks,
                                      const struct itimerval *timer)
{
    long long remaining;
    long long elapsed;

    remaining = (long long)timer->it_value.tv_sec * MICROSECONDS_PER_SECOND;
    remaining += timer->it_value.tv_usec;

    elapsed = (long long)ticks * MICROSECONDS_PER_SECOND;
    elapsed += MICROSECONDS_PER_SECOND - remaining;

    return elapsed < 0 ? 0 : elapsed;
}

static void split_duration(long long microseconds, TimerDuration *duration)
{
    duration->seconds = microseconds / MICROSECONDS_PER_SECOND;
    duration->microseconds = microseconds % MICROSECONDS_PER_SECOND;
}

int timer_profile_start(void)
{
    sigset_t timer_signals;
    sigset_t previous_mask;
    int saved_errno = 0;
    int status = 0;

    if (create_timer_signal_set(&timer_signals) == -1) {
        return -1;
    }

    /* block timer signals while counters and handlers are reset */
    if (sigprocmask(SIG_BLOCK, &timer_signals, &previous_mask) == -1) {
        return -1;
    }

    wall_ticks = 0;
    user_ticks = 0;
    total_cpu_ticks = 0;

    /* one second ticks combine with the remaining timer value */
    if (install_handler(SIGALRM, handle_wall_timer) == -1 ||
        install_handler(SIGVTALRM, handle_user_timer) == -1 ||
        install_handler(SIGPROF, handle_total_cpu_timer) == -1 ||
        arm_timer(ITIMER_REAL) == -1 ||
        arm_timer(ITIMER_VIRTUAL) == -1 ||
        arm_timer(ITIMER_PROF) == -1) {
        saved_errno = errno;
        status = -1;
        (void)disarm_timer(ITIMER_REAL);
        (void)disarm_timer(ITIMER_VIRTUAL);
        (void)disarm_timer(ITIMER_PROF);
    }

    if (sigprocmask(SIG_SETMASK, &previous_mask, 0) == -1 && status == 0) {
        saved_errno = errno;
        status = -1;
    }

    if (status == -1) {
        errno = saved_errno;
    }

    return status;
}

int timer_profile_stop(TimerProfile *profile)
{
    struct itimerval wall_timer;
    struct itimerval user_timer;
    struct itimerval total_cpu_timer;
    sigset_t timer_signals;
    sigset_t previous_mask;
    long long wall_microseconds;
    long long user_microseconds;
    long long total_cpu_microseconds;
    long long kernel_microseconds;
    int saved_errno = 0;
    int status = 0;

    if (profile == 0) {
        errno = EINVAL;
        return -1;
    }

    /* block signals so counters and remaining timers form one snapshot */
    if (create_timer_signal_set(&timer_signals) == -1 ||
        sigprocmask(SIG_BLOCK, &timer_signals, &previous_mask) == -1) {
        return -1;
    }

    if (getitimer(ITIMER_REAL, &wall_timer) == -1 ||
        getitimer(ITIMER_VIRTUAL, &user_timer) == -1 ||
        getitimer(ITIMER_PROF, &total_cpu_timer) == -1) {
        saved_errno = errno;
        status = -1;
    }

    if (disarm_timer(ITIMER_REAL) == -1 ||
        disarm_timer(ITIMER_VIRTUAL) == -1 ||
        disarm_timer(ITIMER_PROF) == -1) {
        if (status == 0) {
            saved_errno = errno;
        }
        status = -1;
    }

    if (sigprocmask(SIG_SETMASK, &previous_mask, 0) == -1) {
        if (status == 0) {
            saved_errno = errno;
        }
        status = -1;
    }

    if (status == -1) {
        errno = saved_errno;
        return -1;
    }

    wall_microseconds = elapsed_microseconds(wall_ticks, &wall_timer);
    user_microseconds = elapsed_microseconds(user_ticks, &user_timer);
    total_cpu_microseconds = elapsed_microseconds(total_cpu_ticks,
                                                  &total_cpu_timer);
    /* derive kernel time from total cpu time after measuring user time */
    kernel_microseconds = total_cpu_microseconds - user_microseconds;

    if (kernel_microseconds < 0) {
        kernel_microseconds = 0;
    }

    split_duration(wall_microseconds, &profile->wall_time);
    split_duration(total_cpu_microseconds, &profile->total_cpu_time);
    split_duration(user_microseconds, &profile->user_time);
    split_duration(kernel_microseconds, &profile->kernel_time);

    return 0;
}

void timer_profile_print(const TimerProfile *profile)
{
    if (profile == 0) {
        return;
    }

    printf("Wall Time Spent Executing : %lld seconds, %lld microseconds\n",
           profile->wall_time.seconds,
           profile->wall_time.microseconds);
    printf("Total Time Spent on CPU : %lld seconds, %lld microseconds\n",
           profile->total_cpu_time.seconds,
           profile->total_cpu_time.microseconds);
    printf("Time Spent in User-Space : %lld seconds, %lld microseconds\n",
           profile->user_time.seconds,
           profile->user_time.microseconds);
    printf("Time Spent in Kernel-Space: %lld seconds, %lld microseconds\n",
           profile->kernel_time.seconds,
           profile->kernel_time.microseconds);
}
