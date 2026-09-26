#include "path_resolver.h"

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <unistd.h>

static char *copy_string(const char *text)
{
    size_t length = strlen(text) + 1;
    char *copy = malloc(length);

    if (copy == NULL) {
        perror("malloc");
        return NULL;
    }

    memcpy(copy, text, length);
    return copy;
}

static int is_executable_file(const char *path)
{
    struct stat file_status;

    return stat(path, &file_status) == 0
        && S_ISREG(file_status.st_mode)
        && access(path, X_OK) == 0;
}

static char *build_candidate_path(const char *directory,
                                  size_t directory_length,
                                  const char *command)
{
    size_t command_length = strlen(command);
    size_t actual_directory_length = directory_length == 0
        ? 1
        : directory_length;

    /* protect the allocation size calculation */
    if (command_length > SIZE_MAX - 2
        || actual_directory_length > SIZE_MAX - command_length - 2) {
        return NULL;
    }

    size_t candidate_length = actual_directory_length + command_length + 2;
    char *candidate = malloc(candidate_length);

    if (candidate == NULL) {
        perror("malloc");
        return NULL;
    }

    if (directory_length == 0) {
        candidate[0] = '.';
    } else {
        memcpy(candidate, directory, directory_length);
    }

    candidate[actual_directory_length] = '/';
    memcpy(candidate + actual_directory_length + 1,
           command,
           command_length + 1);

    return candidate;
}

char *find_command(const char *command)
{
    /* paths containing a slash bypass path lookup */
    if (strchr(command, '/') != NULL) {
        return is_executable_file(command) ? copy_string(command) : NULL;
    }

    const char *path = getenv("PATH");
    if (path == NULL) {
        return NULL;
    }

    const char *directory_start = path;

    /* scan every path field including empty fields */
    while (1) {
        const char *separator = strchr(directory_start, ':');
        size_t directory_length = separator == NULL
            ? strlen(directory_start)
            : (size_t)(separator - directory_start);
        /* an empty path field represents the current directory */
        char *candidate = build_candidate_path(directory_start,
                                                directory_length,
                                                command);

        if (candidate != NULL) {
            if (is_executable_file(candidate)) {
                return candidate;
            }
            free(candidate);
        }

        if (separator == NULL) {
            break;
        }

        directory_start = separator + 1;
    }

    return NULL;
}
