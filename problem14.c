// Project Euler problem 10: https://projecteuler.net/problem=10
// Author: Tom Harkness
// May 29, 2021

#include <stdio.h>
#include <stdbool.h>

#define START_LIMIT 1000000

int chain_length(long int n) {
    int len = 1;
    while (n!= 1) {
        if (n % 2 == 0) {
            n /= 2;
        }
        else { 
            n = 3*n + 1;
        }
        len++;
    }
    return len;
}

int main(void) {
    int best_start = 0;
    int best_length = 0;
    int length;

    for (long int i = 1; i < START_LIMIT; i++)
    {
        length = chain_length(i);
        if (length > best_length) {
            best_start = i;
            best_length = length;
        }
        length = 1;
    }

    printf("best start: %d\n", best_start);
    printf("best length: %d\n", best_length);
}