#ifndef EXECUTOR_H
#define EXECUTOR_H

#include "parser.h"

void execute_simple_command(const Command *command, const char *output_file);
void execute_pipeline(const ParsedLine *parsed);

#endif
