# Project Euler problem 34: https://projecteuler.net/problem=34
# Author: Tom Harkness
# May 29, 2021

from math import factorial as f

def factorial_digit_sum(n):
    res = 0
    for d in str(n):
        res += f(int(d))
    return res

if __name__ == "__main__":
    # found this upper limit by observing:
    # 9999999 -> 9! + ... + 9! = 2540160
    upper_limit = 10**7
    total_sum = 0

    for i in range(3, upper_limit):
        if factorial_digit_sum(i) == i:
            print(f"found: {i}")
            total_sum += i
    print(total_sum)