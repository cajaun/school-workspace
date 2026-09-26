CC ?= cc
CFLAGS ?= -std=c11 -Wall -Wextra -Wpedantic

TARGET = myshell
SOURCES = myshell.c parser.c path_resolver.c executor.c input.c
OBJECTS = $(SOURCES:.c=.o)

.PHONY: all clean

all: $(TARGET)

$(TARGET): $(OBJECTS)
	$(CC) $(CFLAGS) $(OBJECTS) -o $(TARGET)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(TARGET) $(OBJECTS)
