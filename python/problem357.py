# Project Euler problem 357: https://projecteuler.net/problem=357
# Author: Tom Harkness
# July 1, 2021

from itertools import combinations
from math import prod

def divisors(n):
    pf = primeFactors(n)
    divs = set([1])
    for k in range(1,len(pf)+1):
        for c in combinations(pf, k):
            divs.add(prod(c))
    return sorted(list(divs))

def primeFactors(n):
    """returns a list of prime factors of n, repeats allowed"""
    pfactors = []

    if n == 1:
        return []
    if n == 2:
        return [2]
    if n % 2 == 0:
        while n % 2 == 0:
            n //= 2
            pfactors.append(2)
    i = 3
    while (i*i<=n):
        if n % i == 0:
            while n % i == 0:
                n //= i
                pfactors.append(i)
        i += 2
    if n != 1:
        pfactors.append(n)
    return pfactors

def sieve_of_eratosthenes(limit):
    """returns a list of the primes under `limit`"""
    numbers = [False]*2 + (limit-1)*[True]

    n = 2
    while n*n <= limit:
        if numbers[n]:
            m = n*n
            while m <= limit:
                numbers[m] = False
                m += n
        n += 1
    return list([_ for _ in range(len(numbers)) if numbers[_]])

def prime_generating(n):
    for d in divisors(n):
        if not d + n//d in primes:
            return False
    return True

if __name__ == "__main__":
    limit = int(1e8)
    primes = set(sieve_of_eratosthenes(limit))
    div_table = dict()
    answer = 0
    for n in range(1,limit+1):
        if n % 10000 == 0:
            print(n)
        if prime_generating(n):
            answer += n
    print(answer)