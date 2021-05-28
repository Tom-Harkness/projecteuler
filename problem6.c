// Project Euler problem 5: https://projecteuler.net/problem=5
// Author: Tom Harkness
// May 29, 2021

#include <stdbool.h>
#include <stdio.h>

int main(void) {
    int sumOfSquares = 0;
    int squareOfSums = 0;
    int limit = 100;

    for (int i = 1; i<=limit; i++) {
        sumOfSquares += i*i;
        squareOfSums += i;
    }

    squareOfSums *= squareOfSums;

    printf("%d", squareOfSums-sumOfSquares);
}