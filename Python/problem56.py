# Project Euler problem 56: https://projecteuler.net/problem=56
# Author: Tom Harkness
# May 31, 2021

def digit_sum(n):
    dsum = 0
    while n != 0:
        dsum += n % 10
        n //= 10
    return dsum

if __name__ == "__main__":
    best = 0
    for a in range(1, 100):
        for b in range(1, 100):
            dsum = digit_sum(a**b)
            best = max(best, dsum)
    print(best)