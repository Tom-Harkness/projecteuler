// Project Euler problem 27: https://projecteuler.net/problem=27
// Author: Tom Harkness
// May 30, 2021

#include <stdio.h>
#include <stdbool.h>

bool isPrime(int n) {
    """return true if abs(n) is a prime"""
    if (n == 2) {
        return true;
    }
    if (n % 2 == 0) {
        return false;
    }
    for (long int i = 3; i*i*i*i<=n*n; i+=2) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int quadratic_result(int a, int b, int n) {
    return (n*n + a*n + b);
}

int longest_prime_run(int a, int b) {
    int n = 0;
    int primeCount = 0;

    while (true) {
        if (isPrime(quadratic_result(a, b, n))) {
            n += 1;
            primeCount += 1;
        }
        else {
            return primeCount;
        }
    }
}

int main(void) {
    int best = 0;
    int best_a = 0;
    int best_b = 0;

    for (int a = -999; a <= 999; a++) {
        for (int b = -1000; b <= 1000; b++) {
            int run = longest_prime_run(a, b);
            if (run > best) {
                //printf("%d - %d - %d\n", a, b, run);
                best = run;
                best_a = a;
                best_b = b;
            }
        }
    }

    printf("longest run: %d\n", best);
    printf("best a: %d, best b: %d, answer: %d\n", best_a, best_b, best_a*best_b);
}