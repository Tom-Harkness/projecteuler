# Project Euler problem 71: https://projecteuler.net/problem=71
# Author: Tom Harkness
# June 18, 2021

from fractions import Fraction

if __name__ == "__main__":
    d_max =  10**6
    min_distance = 1
    target_frac = Fraction()
    for d in range(d_max, 2, -1):
        for n in range(1,d):
            f = Fraction(n,d)
            if f >= Fraction(3,7):
                break
            distance = Fraction(3,7) - f
            if distance < min_distance:
                min_distance = distance
                target_frac = f
                print(target_frac)
    print(target_frac)