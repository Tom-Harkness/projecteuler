// Project Euler problem 1: https://projecteuler.net/problem=1
// Author: Tom Harkness
// May 27, 2021

#include <stdio.h>

int main(void) {
    size_t result = 0;
    
    for (size_t i = 0; i < 1000; i++) {
        if (i % 3 == 0 || i % 5 == 0) {
            result += i;
        }
    }

    printf("answer: %zu", result);
    return 0;
}
    