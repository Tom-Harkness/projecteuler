# Project Euler problem 73: https://projecteuler.net/problem=73
# Author: Tom Harkness
# June 18, 2021

from fractions import Fraction

if __name__ == "__main__":
    values = list()
    d_max =  12000
    for d in range(2,d_max+1):
        print(d)
        for n in range(1,d):
            f = Fraction(n,d)
            if f > Fraction(1,3) and f < Fraction(1,2):
                values.append(f)
    print(len(set(values)))