# Project Euler problem 99: https://projecteuler.net/problem=99
# Author: Tom Harkness
# May 30, 2021

from math import log
from decimal import Decimal, getcontext

def calculate_row(base, exp):
    # if a**b > c ** d then b*log(a) > d*log(c)
    # so we can calculate the latter instead to find the largest value of base**exp
    return exponent*log(base)


if __name__ == "__main__":
    with open("Python/p099_base_exp.txt", 'r') as f:
        num_string_pairs = [row.strip('\n').split(',') for row in f.readlines()]
        for i in range(len(num_string_pairs)):
            for j in range(len(num_string_pairs[i])):
                num_string_pairs[i][j] = int(num_string_pairs[i][j])

    best_row = 0
    best = 0
    for row_num in range(len(num_string_pairs)):
        base, exponent = num_string_pairs[row_num]
        row_result = calculate_row(base, exponent)
        if row_result > best:
            best_row = row_num + 1
            best = row_result

    print(best_row)
