// Project Euler problem 3: https://projecteuler.net/problem=3
// Author: Tom Harkness
// May 27, 2021

#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <math.h>



bool isPrime(long int n) {
    if (n == 2) {
        return true;
    }
    for (long int i = 3; i*i<=n; i+=2) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

long int largestPrimeFactor(long int n) {
    for (long int i = sqrt(n) + 1; i>=2; i-=1) {
        if (n % i == 0) {
            if (isPrime(i)) {
                return i;   
            }   
        }
    }
    return n;
}

int main(void) {
    long int input = 600851475143;
    
    printf("%li\n", largestPrimeFactor(input));
    return 0;
}