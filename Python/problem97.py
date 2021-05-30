# Project Euler problem 97: https://projecteuler.net/problem=97
# Author: Tom Harkness
# May 30, 2021
# Purpose: Find the last ten digits of the prime 28433*2**7830457 + 1

if __name__ == "__main__":
    result = 28433
    for exponent in range(7830457):
        result *= 2
        result %= 10**10
    result += 1

    print(result)