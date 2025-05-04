# Project Euler problem 48: https://projecteuler.net/problem=48
# Author: Tom Harkness
# May 29, 2021

if __name__ == "__main__":
    result = 0
    for i in range(1, 1001):
        result = (result + i**i) % 10**10
    print(result)