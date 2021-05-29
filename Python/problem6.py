# Project Euler problem 6: https://projecteuler.net/problem=6
# Author: Tom Harkness
# May 29, 2021

if __name__ == "__main__":
    sum_of_squares = sum([x**2 for x in range(1,101)])
    square_of_sums = sum([x for x in range(1,101)])**2

    print(square_of_sums - sum_of_squares)