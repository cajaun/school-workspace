CC ?= cc
CFLAGS ?= -std=c11 -Wall -Wextra -Wpedantic

TARGET = fibonacci_timers
SOURCES = Fibonacci_timers.c fibonacci.c timer_profile.c
OBJECTS = $(SOURCES:.c=.o)

.PHONY: all clean

all: $(TARGET)

$(TARGET): $(OBJECTS)
	$(CC) $(CFLAGS) $(OBJECTS) -o $(TARGET)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(TARGET) $(OBJECTS)
