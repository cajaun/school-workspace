#include "executor.h"
#include "input.h"
#include "parser.h"

#include <stdio.h>
#include <string.h>

int main(void)
{
    char line[MAX_LINE];

    while (1) {
        printf("[Enter command]>");
        fflush(stdout);

        int read_status = read_command_line(line, sizeof(line));
        if (read_status == 0) {
            printf("\n");
            break;
        }
        if (read_status < 0) {
            continue;
        }

        ParsedLine parsed;
        ParseResult result = parse_line(line, &parsed);
        if (result == PARSE_EMPTY) {
            continue;
        }
        if (result != PARSE_OK) {
            print_parse_error(result);
            continue;
        }

        if (!parsed.has_pipe
            && parsed.output_file == NULL
            && parsed.first.argument_count == 1
            && strcmp(parsed.first.arguments[0], "exit") == 0) {
            break;
        }

        if (parsed.has_pipe) {
            execute_pipeline(&parsed);
        } else {
            execute_simple_command(&parsed.first, parsed.output_file);
        }
    }

    return 0;
}
