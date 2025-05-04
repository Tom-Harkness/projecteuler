# Project Euler problem 2: https://projecteuler.net/problem=2
# Author: Tom Harkness
# May 29, 2021

if __name__ == "__main__":
    a, b = 1, 2
    result = b

    while a+b <= 4e6:
        a, b = b, a+b
        if b % 2 == 0:
            result += b
    print(result)
