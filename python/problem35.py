# Project Euler problem 35: https://projecteuler.net/problem=35
# Author: Tom Harkness
# May 31, 2021

from itertools import permutations

def sieve_of_eratosthenes(limit):
    numbers = (limit+1)*[True]
    numbers[0] = False
    numbers[1] = False

    n = 2
    while n*n <= limit:
        if numbers[n]:
            m = n*n
            while m <= limit:
                numbers[m] = False
                m += n
        n += 1
    return [_ for _ in range(len(numbers)) if numbers[_]]

def isCircular(prime):
    digits = len(prime)
    for _ in range(digits):
        prime = prime[1:] + prime[0]
        if prime not in prime_strings:
            return False
    return True

if __name__ == "__main__":
    limit = 10**6
    prime_strings = [str(p) for p in sieve_of_eratosthenes(limit)]

    print(sum(map(isCircular, prime_strings)))