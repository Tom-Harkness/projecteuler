# Project Euler problem 20: https://projecteuler.net/problem=20
# Author: Tom Harkness
# May 29, 2021

from math import factorial

if __name__ == "__main__":
    print(sum( [int(d) for d in list(str(factorial(100)))]))