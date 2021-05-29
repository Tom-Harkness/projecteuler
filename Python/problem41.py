# Project Euler problem 41: https://projecteuler.net/problem=41
# Author: Tom Harkness
# May 29, 2021

from itertools import permutations


def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n**0.5+1), 2):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    # 9-digit and 8-digit pandigitals were all tested and showed no primes
    digits = '1234567'
    pandigital_numbers = [int(''.join(p)) for p in permutations(digits)][::-1]
    for n in pandigital_numbers:
        print(f"testing {n}")
        if isPrime(n):
            print(f"found a prime: {n}")
            break