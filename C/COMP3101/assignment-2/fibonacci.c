#include "fibonacci.h"

#include <limits.h>

static int fibonacci_recursive(unsigned int index,
                               unsigned long long *result)
{
    unsigned long long previous;
    unsigned long long before_previous;

    if (result == 0) {
        return FIBONACCI_INVALID_ARGUMENT;
    }

    if (index == 0) {
        *result = 0;
        return FIBONACCI_SUCCESS;
    }

    if (index == 1 || index == 2) {
        *result = 1;
        return FIBONACCI_SUCCESS;
    }

    if (fibonacci_recursive(index - 1, &previous) != FIBONACCI_SUCCESS) {
        return FIBONACCI_OVERFLOW;
    }

    if (fibonacci_recursive(index - 2, &before_previous) != FIBONACCI_SUCCESS) {
        return FIBONACCI_OVERFLOW;
    }

    /* check before adding so overflow cannot corrupt the recursive result */
    if (ULLONG_MAX - previous < before_previous) {
        return FIBONACCI_OVERFLOW;
    }

    *result = previous + before_previous;
    return FIBONACCI_SUCCESS;
}

int fibonacci_compute(unsigned int index, unsigned long long *result)
{
    return fibonacci_recursive(index, result);
}
