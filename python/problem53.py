# Project Euler problem 53: https://projecteuler.net/problem=53
# Author: Tom Harkness
# June 17, 2021

from math import comb

if __name__ == "__main__":
    count = 0
    for n in range(1,101):
        for r in range(1, n+1):
            if comb(n,r) > 10**6:
                count += 1
    print(count)