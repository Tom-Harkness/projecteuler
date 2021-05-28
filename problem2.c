// Project Euler problem 2: https://projecteuler.net/problem=2
// Author: Tom Harkness
// May 27, 2021

#include <stdio.h>
#include <stdint.h>

int fib(uint32_t f_n, uint32_t f_m) {
    
    // return the next term in the Fibonacci sequence
    return f_n + f_m;
}

int main(void) {
    uint32_t f_0 = 1;
    uint32_t f_1 = 2;
    uint32_t result = f_1;

    uint32_t f_next = fib(f_0, f_1);

    while (f_next < 4000000) {
        if (f_next % 2 == 0) {
            result += f_next;
        }

        f_0 = f_1;
        f_1 = f_next;
        f_next = fib(f_0, f_1);
    }

    printf("%u", result);
    return 0;
}