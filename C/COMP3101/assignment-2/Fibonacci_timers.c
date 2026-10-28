#include "fibonacci.h"
#include "timer_profile.h"

#include <errno.h>
#include <limits.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

static void print_usage(const char *program_name)
{
    fprintf(stderr, "Usage: %s <parent_n> <child_1_n> <child_2_n>\n",
            program_name);
}

static int parse_index(const char *text, unsigned int *index)
{
    char *end;
    unsigned long long parsed;

    if (text == 0 || index == 0 || *text == '\0') {
        return -1;
    }

    errno = 0;
    parsed = strtoull(text, &end, 10);
    if (errno == ERANGE || *end != '\0' || parsed == 0 ||
        parsed > UINT_MAX) {
        return -1;
    }

    *index = (unsigned int)parsed;
    return 0;
}

static int run_child(const char *label, unsigned int index)
{
    TimerProfile profile;
    unsigned long long result;
    int calculation_status;

    /* restart timers so child measurements start from zero */
    if (timer_profile_start() == -1) {
        perror("timer_profile_start");
        return EXIT_FAILURE;
    }

    calculation_status = fibonacci_compute(index, &result);
    if (timer_profile_stop(&profile) == -1) {
        perror("timer_profile_stop");
        return EXIT_FAILURE;
    }

    if (calculation_status != FIBONACCI_SUCCESS) {
        fprintf(stderr, "%s could not compute fibonacci(%u)\n",
                label, index);
        return EXIT_FAILURE;
    }

    printf("[%s] fibonacci(%u) = %llu\n", label, index, result);
    timer_profile_print(&profile);
    return fflush(stdout) == EOF ? EXIT_FAILURE : EXIT_SUCCESS;
}

static int wait_for_child(pid_t child_pid, const char *label)
{
    int status;
    pid_t waited_pid;

    do {
        waited_pid = waitpid(child_pid, &status, 0);
    } while (waited_pid == -1 && errno == EINTR);

    if (waited_pid == -1) {
        perror("waitpid");
        return -1;
    }

    if (WIFEXITED(status) && WEXITSTATUS(status) == EXIT_SUCCESS) {
        return 0;
    }

    if (WIFSIGNALED(status)) {
        fprintf(stderr, "%s ended from signal %d\n",
                label, WTERMSIG(status));
    } else {
        fprintf(stderr, "%s ended with a failure status\n", label);
    }

    return -1;
}

static void terminate_child(pid_t child_pid)
{
    if (kill(child_pid, SIGTERM) == -1 && errno != ESRCH) {
        perror("kill");
    }

    (void)wait_for_child(child_pid, "Child 1");
}

int main(int argc, char *argv[])
{
    TimerProfile parent_profile;
    unsigned long long parent_result;
    unsigned int parent_index;
    unsigned int child_one_index;
    unsigned int child_two_index;
    pid_t child_one;
    pid_t child_two;
    int parent_calculation_status;
    int child_one_status;
    int child_two_status;
    int exit_status = EXIT_SUCCESS;

    if (argc != 4 ||
        parse_index(argv[1], &parent_index) == -1 ||
        parse_index(argv[2], &child_one_index) == -1 ||
        parse_index(argv[3], &child_two_index) == -1) {
        print_usage(argv[0]);
        return EXIT_FAILURE;
    }

    /* start before fork so the parent profile includes child work and waiting */
    if (timer_profile_start() == -1) {
        perror("timer_profile_start");
        return EXIT_FAILURE;
    }

    /* create both children before the parent begins its own calculation */
    fflush(0);
    child_one = fork();
    if (child_one == -1) {
        perror("fork");
        (void)timer_profile_stop(&parent_profile);
        return EXIT_FAILURE;
    }

    if (child_one == 0) {
        _exit(run_child("Child 1", child_one_index));
    }

    fflush(0);
    child_two = fork();
    if (child_two == -1) {
        perror("fork");
        terminate_child(child_one);
        (void)timer_profile_stop(&parent_profile);
        return EXIT_FAILURE;
    }

    if (child_two == 0) {
        _exit(run_child("Child 2", child_two_index));
    }

    /* wait after computing so the parent profile includes child completion time */
    parent_calculation_status = fibonacci_compute(parent_index, &parent_result);
    child_one_status = wait_for_child(child_one, "Child 1");
    child_two_status = wait_for_child(child_two, "Child 2");

    if (timer_profile_stop(&parent_profile) == -1) {
        perror("timer_profile_stop");
        return EXIT_FAILURE;
    }

    if (parent_calculation_status != FIBONACCI_SUCCESS) {
        fprintf(stderr, "Parent could not compute fibonacci(%u)\n",
                parent_index);
        exit_status = EXIT_FAILURE;
    } else {
        printf("[Parent] fibonacci(%u) = %llu\n",
               parent_index, parent_result);
        timer_profile_print(&parent_profile);
    }

    if (child_one_status == -1 || child_two_status == -1) {
        exit_status = EXIT_FAILURE;
    }

    return exit_status;
}
