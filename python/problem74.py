# Project Euler problem 74: https://projecteuler.net/problem=74
# Author: Tom Harkness
# June 17, 2021

from math import factorial as fac


def digit_factorial_sum(n):
    dsum = 0
    while n != 0:
        dsum += fac(n % 10)
        n //= 10
    return dsum


def measure_chain(start_n):
    seen_values = [start_n]
    n = digit_factorial_sum(start_n)
    count = 1
    while count <= 61:
        if n in seen_values:
            return len(seen_values)
        else:
            seen_values.append(n)
            count += 1
            n = digit_factorial_sum(n)
    

if __name__ == "__main__":
    #print(digit_factorial_sum(145))
    count = 0
    for n in range(2,1000001):
        if n % 10000 == 0:
            print(f"searching past: {n}")
        if measure_chain(n) == 60:
            count += 1
            print(n)
    print(count)