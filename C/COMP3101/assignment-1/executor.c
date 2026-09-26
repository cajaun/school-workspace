#include "executor.h"

#include "path_resolver.h"

#include <errno.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

static int redirect_output(const char *output_file)
{
    /* redirect output inside the child so the shell keeps its prompt */
    int file_descriptor = open(output_file,
                               O_WRONLY | O_CREAT | O_TRUNC,
                               0644);

    if (file_descriptor < 0) {
        perror("open");
        return -1;
    }

    if (file_descriptor != STDOUT_FILENO
        && dup2(file_descriptor, STDOUT_FILENO) < 0) {
        perror("dup2");
        close(file_descriptor);
        return -1;
    }

    if (file_descriptor != STDOUT_FILENO) {
        close(file_descriptor);
    }

    return 0;
}

static void close_child_descriptors(const int descriptors[],
                                    size_t descriptor_count)
{
    /* both pipeline children inherit both pipe ends */
    for (size_t index = 0; index < descriptor_count; index++) {
        if (descriptors[index] > STDERR_FILENO) {
            close(descriptors[index]);
        }
    }
}

static pid_t spawn_command(const char *program,
                           char *const arguments[],
                           int input_fd,
                           int output_fd,
                           const char *output_file,
                           const int inherited_descriptors[],
                           size_t inherited_descriptor_count)
{
    pid_t process_id = fork();

    if (process_id < 0) {
        perror("fork");
        return -1;
    }

    if (process_id == 0) {
        /* connect streams before closing the inherited pipe descriptors */
        if (input_fd != STDIN_FILENO && dup2(input_fd, STDIN_FILENO) < 0) {
            perror("dup2");
            _exit(EXIT_FAILURE);
        }

        if (output_fd != STDOUT_FILENO && dup2(output_fd, STDOUT_FILENO) < 0) {
            perror("dup2");
            _exit(EXIT_FAILURE);
        }

        close_child_descriptors(inherited_descriptors,
                                inherited_descriptor_count);

        if (output_file != NULL && redirect_output(output_file) < 0) {
            _exit(EXIT_FAILURE);
        }

        execv(program, arguments);
        perror("execv");
        _exit(EXIT_FAILURE);
    }

    return process_id;
}

static void wait_for_process(pid_t process_id)
{
    /* signals can interrupt a blocking wait */
    while (waitpid(process_id, NULL, 0) < 0) {
        if (errno != EINTR) {
            perror("waitpid");
            break;
        }
    }
}

static void report_missing_command(const char *command)
{
    fprintf(stderr, "%s: command not found\n", command);
}

static int create_pipe(int pipe_fds[2])
{
    if (pipe(pipe_fds) < 0) {
        perror("pipe");
        return -1;
    }

    /* keep pipe descriptors separate from standard streams */
    for (size_t index = 0; index < 2; index++) {
        if (pipe_fds[index] <= STDERR_FILENO) {
            int duplicate = fcntl(pipe_fds[index],
                                  F_DUPFD,
                                  STDERR_FILENO + 1);
            if (duplicate < 0) {
                perror("fcntl");
                close(pipe_fds[0]);
                close(pipe_fds[1]);
                return -1;
            }

            close(pipe_fds[index]);
            pipe_fds[index] = duplicate;
        }
    }

    return 0;
}

void execute_simple_command(const Command *command,
                            const char *output_file)
{
    char *program = find_command(command->arguments[0]);
    if (program == NULL) {
        report_missing_command(command->arguments[0]);
        return;
    }

    pid_t process_id = spawn_command(program,
                                     command->arguments,
                                     STDIN_FILENO,
                                     STDOUT_FILENO,
                                     output_file,
                                     NULL,
                                     0);

    if (process_id >= 0) {
        wait_for_process(process_id);
    }

    free(program);
}

void execute_pipeline(const ParsedLine *parsed)
{
    char *first_program = find_command(parsed->first.arguments[0]);
    char *second_program = find_command(parsed->second.arguments[0]);

    if (first_program == NULL) {
        report_missing_command(parsed->first.arguments[0]);
        free(second_program);
        return;
    }

    if (second_program == NULL) {
        report_missing_command(parsed->second.arguments[0]);
        free(first_program);
        return;
    }

    int pipe_fds[2];
    if (create_pipe(pipe_fds) < 0) {
        free(first_program);
        free(second_program);
        return;
    }

    /* connect the first writer to the second reader */
    pid_t first_process = spawn_command(first_program,
                                        parsed->first.arguments,
                                        STDIN_FILENO,
                                        pipe_fds[1],
                                        NULL,
                                        pipe_fds,
                                        2);

    if (first_process < 0) {
        close(pipe_fds[0]);
        close(pipe_fds[1]);
        free(first_program);
        free(second_program);
        return;
    }

    pid_t second_process = spawn_command(second_program,
                                         parsed->second.arguments,
                                         pipe_fds[0],
                                         STDOUT_FILENO,
                                         parsed->output_file,
                                         pipe_fds,
                                         2);

    if (second_process < 0) {
        close(pipe_fds[0]);
        close(pipe_fds[1]);
        wait_for_process(first_process);
        free(first_program);
        free(second_program);
        return;
    }

    /* the parent must close both ends so readers can observe end of input */
    close(pipe_fds[0]);
    close(pipe_fds[1]);
    wait_for_process(first_process);
    wait_for_process(second_process);

    free(first_program);
    free(second_program);
}
