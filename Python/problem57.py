# Project Euler problem 57: https://projecteuler.net/problem=57
# Author: Tom Harkness
# June 18, 2021

import sys
from fractions import Fraction

def iterate(max_iterations, current_depth):
    if max_iterations == current_depth:
        return Fraction(2)
    return Fraction(2 + 1/iterate(max_iterations, current_depth + 1))

def check_property(frac):
    num, den = str(frac).split('/')
    return len(num) > len(den)

def calculate_expansion(depth):
    sqrt_2 = 1 + 1/iterate(depth, 1)
    return sqrt_2

if __name__ == "__main__":
    sys.setrecursionlimit(1100)
    answer_count = 0

    for depth in range(1,1001):
        print(depth)
        frac = calculate_expansion(depth)
        if check_property(frac):
            answer_count += 1

    print(answer_count)
