# COMP3101 Assignment 1

This assignment implements a small command shell in C. The program reads one command at a time, parses its arguments, resolves commands through `PATH`, creates child processes, and waits for foreground work to finish.

## Supported Shell Work

| Feature | Implementation area |
| --- | --- |
| Input collection | `input.c` and `input.h` |
| Command and operator parsing | `parser.c` and `parser.h` |
| PATH resolution | `path_resolver.c` and `path_resolver.h` |
| Process execution and file descriptors | `executor.c` and `executor.h` |
| Interactive loop | `myshell.c` |

The shell handles simple commands with arguments, output redirection, one pipe, and pipe output redirection. It uses `fork`, `execv`, `dup2`, `pipe`, `open`, and `waitpid` for process control.

## Build and Run

~~~bash
make
./myshell
~~~

The Makefile produces `myshell` and the object files for each module. Remove generated output with:

~~~bash
make clean
~~~

## Example Commands

~~~text
ls
ls -l
ls -l > file_list.txt
ls -l | wc -l
ls -l | wc -l > numfiles.txt
exit
~~~

Run commands from the assignment folder when the command needs a local file path. The shell exits when the user enters `exit`.
