# COMP3101

This course folder contains the Assignment 1 shell implementation and the Lab 1 and Lab 3 process exercises.

## Work Map

| Work | Scope | Guide |
| --- | --- | --- |
| Assignment 1 | Command parsing, PATH lookup, process execution, redirection, and one pipe | [assignment README](assignment-1/README.md) |
| Lab 1 | Basic C output and command-line arguments | [lab 1 folder](lab-1/) |
| Lab 3 | `fork`, process identifiers, `execl`, and `wait` | [lab 3 folder](lab-3/) |

## Toolchain

The Makefiles use C11 with `-Wall`, `-Wextra`, and `-Wpedantic`.

Run a target from its own folder:

~~~bash
cd assignment-1
make
./myshell
~~~

Remove local build output with `make clean`.
