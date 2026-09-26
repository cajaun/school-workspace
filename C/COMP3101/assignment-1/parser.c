#include "parser.h"

#include <ctype.h>
#include <stdio.h>
#include <string.h>

static char *trim_whitespace(char *text)
{
    while (isspace((unsigned char)*text)) {
        text++;
    }

    char *end = text + strlen(text);
    while (end > text && isspace((unsigned char)end[-1])) {
        end--;
    }

    *end = '\0';
    return text;
}

static ParseResult parse_words(char *text, Command *command)
{
    /* compact parsed text in place to keep argument pointers stable */
    char *reader = text;
    char *writer = text;
    size_t argument_count = 0;

    while (*reader != '\0') {
        while (isspace((unsigned char)*reader)) {
            reader++;
        }

        if (*reader == '\0') {
            break;
        }

        if (argument_count >= MAX_ARGS - 1) {
            return PARSE_TOO_MANY_ARGUMENTS;
        }

        command->arguments[argument_count++] = writer;
        char quote = '\0';

        while (*reader != '\0') {
            char current = *reader;

            if (quote == '\0' && isspace((unsigned char)current)) {
                break;
            }

            /* remove escapes and quotes while preserving literal characters */
            if (current == '\\') {
                if (reader[1] == '\0') {
                    return PARSE_INVALID_ESCAPE;
                }

                *writer++ = reader[1];
                reader += 2;
                continue;
            }

            if (current == '\'' || current == '"') {
                if (quote == '\0') {
                    quote = current;
                } else if (quote == current) {
                    quote = '\0';
                } else {
                    *writer++ = current;
                }

                reader++;
                continue;
            }

            *writer++ = current;
            reader++;
        }

        if (quote != '\0') {
            return PARSE_UNMATCHED_QUOTE;
        }

        /* skip the delimiter before writing the terminator */
        while (isspace((unsigned char)*reader)) {
            reader++;
        }

        *writer++ = '\0';
    }

    command->arguments[argument_count] = NULL;
    command->argument_count = argument_count;

    return argument_count == 0 ? PARSE_EMPTY : PARSE_OK;
}

static ParseResult locate_operators(char *line,
                                    char **pipe_symbol,
                                    char **redirect_symbol)
{
    char quote = '\0';

    *pipe_symbol = NULL;
    *redirect_symbol = NULL;

    /* scan before editing the buffer so quoted operators stay literal */
    for (char *cursor = line; *cursor != '\0'; cursor++) {
        if (*cursor == '\\') {
            if (cursor[1] == '\0') {
                return PARSE_INVALID_ESCAPE;
            }

            cursor++;
            continue;
        }

        if (quote != '\0') {
            if (*cursor == quote) {
                quote = '\0';
            }
            continue;
        }

        if (*cursor == '\'' || *cursor == '"') {
            quote = *cursor;
            continue;
        }

        if (*cursor == '|') {
            if (*pipe_symbol != NULL) {
                return PARSE_SYNTAX_ERROR;
            }

            *pipe_symbol = cursor;
        } else if (*cursor == '>') {
            if (*redirect_symbol != NULL) {
                return PARSE_SYNTAX_ERROR;
            }

            *redirect_symbol = cursor;
        }
    }

    if (quote != '\0') {
        return PARSE_UNMATCHED_QUOTE;
    }

    /* keep output redirection at the end of the supported command form */
    if (*pipe_symbol != NULL && *redirect_symbol != NULL
        && *redirect_symbol < *pipe_symbol) {
        return PARSE_SYNTAX_ERROR;
    }

    return PARSE_OK;
}

ParseResult parse_line(char *line, ParsedLine *parsed)
{
    char *pipe_symbol;
    char *redirect_symbol;
    ParseResult result = locate_operators(line,
                                          &pipe_symbol,
                                          &redirect_symbol);

    if (result != PARSE_OK) {
        return result;
    }

    memset(parsed, 0, sizeof(*parsed));

    /* isolate the output path before parsing the command segments */
    if (redirect_symbol != NULL) {
        *redirect_symbol = '\0';
        char *file_text = trim_whitespace(redirect_symbol + 1);
        Command file_command;

        result = parse_words(file_text, &file_command);
        if (result == PARSE_EMPTY) {
            return PARSE_MISSING_OUTPUT;
        }
        if (result != PARSE_OK || file_command.argument_count != 1) {
            return result == PARSE_OK ? PARSE_SYNTAX_ERROR : result;
        }
        if (file_command.arguments[0][0] == '\0') {
            return PARSE_MISSING_OUTPUT;
        }

        parsed->output_file = file_command.arguments[0];
    }

    if (pipe_symbol != NULL) {
        *pipe_symbol = '\0';

        result = parse_words(trim_whitespace(line), &parsed->first);
        if (result == PARSE_EMPTY) {
            return PARSE_SYNTAX_ERROR;
        }
        if (result != PARSE_OK) {
            return result;
        }

        result = parse_words(trim_whitespace(pipe_symbol + 1), &parsed->second);
        if (result == PARSE_EMPTY) {
            return PARSE_SYNTAX_ERROR;
        }
        if (result != PARSE_OK) {
            return result;
        }

        parsed->has_pipe = 1;
        return PARSE_OK;
    }

    return parse_words(trim_whitespace(line), &parsed->first);
}

void print_parse_error(ParseResult result)
{
    switch (result) {
        case PARSE_TOO_MANY_ARGUMENTS:
            fprintf(stderr, "Too many arguments\n");
            break;
        case PARSE_UNMATCHED_QUOTE:
            fprintf(stderr, "Unmatched quote\n");
            break;
        case PARSE_INVALID_ESCAPE:
            fprintf(stderr, "Invalid escape sequence\n");
            break;
        case PARSE_MISSING_OUTPUT:
            fprintf(stderr, "Missing output file after >\n");
            break;
        default:
            fprintf(stderr, "Invalid command syntax\n");
            break;
    }
}
