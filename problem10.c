// Project Euler problem 10: https://projecteuler.net/problem=10
// Author: Tom Harkness
// May 29, 2021

#include <stdio.h>
#include <stdbool.h>

#define PRIME_LIMIT 2000000

bool isPrime(long int n) {
    if (n == 0 || n == 1) {
        return false;
    }
    if (n == 2) {
        return true;
    }
    if (n % 2 == 0) {
        return false;
    }
    for (long int i = 3; i*i<=n; i+=2) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int main(void) {
    long int primeSum = 0;

    for (long int i = 0; i < PRIME_LIMIT; i++)
    {
        if (isPrime(i)) {
            primeSum += i;
        }
    }
    printf("%ld\n", primeSum);
}