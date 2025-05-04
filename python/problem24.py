# Project Euler problem 24: https://projecteuler.net/problem=24
# Author: Tom Harkness
# May 29, 2021

from itertools import permutations

if __name__ == "__main__":
    digits = '0123456789'
    print(''.join([p for p in permutations(digits)][999999]))