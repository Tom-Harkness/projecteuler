// Project Euler problem 4: https://projecteuler.net/problem=4
// Author: Tom Harkness
// May 28, 2021

#include <stdbool.h>
#include <stdio.h>

bool isPalindrome(int n) {
    int reverse_n = 0;
    int n_copy = n;

    while (n != 0) {
        reverse_n *= 10;
        reverse_n += n % 10;
        n /= 10;
    }
    
    return (n_copy == reverse_n);
}

int main(void) {
    int best = 0;

    for (int i = 999; i >= 100; i--) {
        for (int j = 999; j >= 100; j--) {
            if (i*j > best) {
                if (isPalindrome(i*j)) {
                    best = i*j;
                }
            }
        }
    }
    printf("%d", best);
    return 0;
}