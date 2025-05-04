# Project Euler problem 1: https://projecteuler.net/problem=1
# Author: Tom Harkness
# May 29, 2021

if __name__ == "__main__":
    print(sum([_ for _ in range(1,1000) if _ % 3 == 0 or _ % 5 == 0]))