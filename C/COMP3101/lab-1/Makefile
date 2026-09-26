CC ?= cc
CFLAGS ?= -std=c11 -Wall -Wextra -Wpedantic

PROGRAMS = first params

.PHONY: all clean

all: $(PROGRAMS)

%: %.c
	$(CC) $(CFLAGS) $< -o $@

clean:
	rm -f $(PROGRAMS)
