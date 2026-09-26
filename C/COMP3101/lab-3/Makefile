CC ?= cc
CFLAGS ?= -std=c11 -Wall -Wextra -Wpedantic

PROGRAMS = simple_fork simple_fork_2 child_pid child_pid_2 overlay_child overlay_child_2 wait_on_child wait_on_child_2

.PHONY: all clean

all: $(PROGRAMS)

%: %.c
	$(CC) $(CFLAGS) $< -o $@

clean:
	rm -f $(PROGRAMS)
