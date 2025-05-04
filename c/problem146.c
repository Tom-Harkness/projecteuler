// Project Euler problem 146: https://projecteuler.net/problem=146
// Author: Tom Harkness
// June 18, 2021

#include <stdio.h>
#include <stdbool.h>

#define lli long long int

bool isPrime(lli n) {
    if (n == 2) {
        return true;
    }
    if (n % 2 == 0) {
        return false;
    }
    for (lli i = 3; i*i*i*i<=n*n; i+=2) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int main(void) {
    lli property_sum = 0;
    for (int n = 2; n < 230000 ; n += 2) {
        if (n%1000 == 0) {
            printf("--%d--\n", n);
        }
        if (isPrime(n*n+1)) {
            if (isPrime(n*n+3)) {
                if (isPrime(n*n+7)) {
                    if (isPrime(n*n+9)) {
                        if (isPrime(n*n+13)) {
                            if (isPrime(n*n+27)) {
                                //printf("%d\n", n);
                                property_sum += n;
                            }
                        }
                    }
                }
            }
        }
    }
    printf("%lld", property_sum);
})