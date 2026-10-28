# COMP3101 Assignment 2

This assignment profiles three processes while they compute recursive Fibonacci values. The parent computes `argv[1]`, Child 1 computes `argv[2]`, and Child 2 computes `argv[3]`.

## Timer Design

The timer module uses POSIX interval timers:

| Measurement | Timer |
| --- | --- |
| Wall time | `ITIMER_REAL` and `SIGALRM` |
| User time | `ITIMER_VIRTUAL` and `SIGVTALRM` |
| Total CPU time | `ITIMER_PROF` and `SIGPROF` |
| Kernel time | Total CPU time minus user time |

Each timer raises a signal at one-second intervals. The signal handlers update `sig_atomic_t` counters. The timer module blocks those signals while it snapshots the remaining timer values.

## Build and Run

~~~bash
make
./fibonacci_timers 10 11 12
~~~

The assignment example uses:

~~~bash
./fibonacci_timers 43 44 45
~~~

Recursive Fibonacci grows fast. Use small values while checking the process order and output format.

Remove generated output with:

~~~bash
make clean
~~~

## Source Layout

| File | Responsibility |
| --- | --- |
| `Fibonacci_timers.c` | Argument validation, process creation, waiting, and output |
| `fibonacci.c` and `fibonacci.h` | Recursive Fibonacci calculation and overflow checks |
| `timer_profile.c` and `timer_profile.h` | Signal handlers, interval timers, duration conversion, and reporting |
| `Makefile` | C11 compilation with strict warnings |
