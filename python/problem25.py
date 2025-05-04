# Project Euler problem 25: https://projecteuler.net/problem=25
# Author: Tom Harkness
# May 29, 2021

from math import log10

if __name__ == "__main__":
    digit_target = 1000
    a, b = 1, 1
    result = b
    i = 3
    while log10(a+b) <= digit_target-1:
        a, b = b, a+b
        i+= 1
    print(i, a+b)