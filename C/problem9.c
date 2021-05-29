// Project Euler problem 9: https://projecteuler.net/problem=9
// Author: Tom Harkness
// May 29, 2021

#include <stdbool.h>
#include <stdio.h>

#define TARGET_SUM 1000

int main(void) {
    for (int a = 1; a < TARGET_SUM; a++) {
        for (int b = 1; b < TARGET_SUM; b++) {
            for (int c = 1; c < TARGET_SUM; c++) {
                if (a*a + b*b - c*c == 0) {
                    if (a + b + c == 1000) {
                        printf("%d", a*b*c);
                        return 0;
                    }
                }
            }   
        }
    }
}