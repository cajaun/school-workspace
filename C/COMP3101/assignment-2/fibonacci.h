#ifndef FIBONACCI_H
#define FIBONACCI_H

enum FibonacciStatus {
    FIBONACCI_SUCCESS = 0,
    FIBONACCI_INVALID_ARGUMENT = 1,
    FIBONACCI_OVERFLOW = 2
};

int fibonacci_compute(unsigned int index, unsigned long long *result);

#endif
