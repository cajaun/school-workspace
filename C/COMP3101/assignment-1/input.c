#include "input.h"

#include <limits.h>
#include <stdio.h>
#include <string.h>

int read_command_line(char *line, size_t line_size)
{
    if (line_size > (size_t)INT_MAX) {
        fprintf(stderr, "Command buffer is too large\n");
        return -1;
    }

    if (fgets(line, (int)line_size, stdin) == NULL) {
        return 0;
    }

    /* reject partial input instead of executing a truncated command */
    if (strchr(line, '\n') == NULL) {
        int character;
        while ((character = getchar()) != '\n' && character != EOF) {
        }

        fprintf(stderr, "Command exceeds maximum length\n");
        return -1;
    }

    line[strcspn(line, "\n")] = '\0';
    return 1;
}
