// Project Euler problem 7: https://projecteuler.net/problem=7
// Author: Tom Harkness
// May 29, 2021

#include <stdbool.h>
#include <stdio.h>

#define PRIME_LIMIT 10001
long int primes[PRIME_LIMIT];

bool isPrime(long int n) {
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

void getPrimes() {
    int primeCount = 0;
    long int i = 2;
    while (primeCount < PRIME_LIMIT) {
        if (isPrime(i) == true) {
            primes[primeCount] = i;
            primeCount += 1;
        }
        i++;
    }
}

int main(void) {
    getPrimes();
    printf("%ld\n", primes[PRIME_LIMIT-1]);
}