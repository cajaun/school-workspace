#ifndef TIMER_PROFILE_H
#define TIMER_PROFILE_H

typedef struct {
    long long seconds;
    long long microseconds;
} TimerDuration;

typedef struct {
    TimerDuration wall_time;
    TimerDuration total_cpu_time;
    TimerDuration user_time;
    TimerDuration kernel_time;
} TimerProfile;

int timer_profile_start(void);
int timer_profile_stop(TimerProfile *profile);
void timer_profile_print(const TimerProfile *profile);

#endif
