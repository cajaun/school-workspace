#ifndef PARSER_H
#define PARSER_H

#include <stddef.h>

#define MAX_ARGS 100

typedef struct {
    char *arguments[MAX_ARGS];
    size_t argument_count;
} Command;

typedef struct {
    Command first;
    Command second;
    char *output_file;
    int has_pipe;
} ParsedLine;

typedef enum {
    PARSE_OK,
    PARSE_EMPTY,
    PARSE_SYNTAX_ERROR,
    PARSE_TOO_MANY_ARGUMENTS,
    PARSE_UNMATCHED_QUOTE,
    PARSE_INVALID_ESCAPE,
    PARSE_MISSING_OUTPUT
} ParseResult;

ParseResult parse_line(char *line, ParsedLine *parsed);
void print_parse_error(ParseResult result);

#endif
