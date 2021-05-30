# Project Euler problem 29: https://projecteuler.net/problem=29
# Author: Tom Harkness
# May 30, 2021

if __name__ == "__main__":
    upper_range = 100

    distinct_terms = len(set([a**b for a in range(2,upper_range+1) for b in range(2,upper_range+1)]))
    print(distinct_terms)
