# Project Euler problem 33: https://projecteuler.net/problem=33
# Author: Tom Harkness
# June 18, 2021

from itertools import combinations
from fractions import Fraction

def try_cancel(n,d):
    n_chars = set(str((n)))
    d_chars = set(str(d))
    common_chars = n_chars.intersection(d_chars)
    if len(common_chars) == 2 or common_chars == set(['0']) or common_chars == set():
        return False # trivial examples
    cancelled_n = n_chars.difference(common_chars)
    cancelled_d = d_chars.difference(common_chars)
    if cancelled_n == set() or cancelled_d == set() or cancelled_n == set(['0']) or cancelled_d == set(['0']):
        return False
    cancelled_fraction = int(max(cancelled_n)) / int(max(cancelled_d))
    return n/d == cancelled_fraction

if __name__ == "__main__":
    fracs = [(n,d) for (n,d) in combinations(range(10,100), 2) if d>n]
    answer_n = 1
    answer_d = 1
    for (n,d) in fracs:
        if try_cancel(n,d):
            print((n,d))
            answer_n *= n
            answer_d *= d
    print(Fraction(answer_n, answer_d))
