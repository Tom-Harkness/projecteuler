# Project Euler problem 49: https://projecteuler.net/problem=49
# Author: Tom Harkness
# May 31, 2021

from itertools import permutations


def sieve_of_eratosthenes(limit):
    """returns a list of the primes under `limit`"""
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


def getPermutations(n):
    return [int(''.join(_)) for _ in permutations(str(n))]


def checkPrimePermutations(p):
    count = 0
    permPrimes = []
    for perm in getPermutations(p):
        #print(perm)
        if perm in primes:
            count += 1
            permPrimes.append(perm)
    permPrimes = sorted(permPrimes)

    for i in range(len(permPrimes)-2):
        for j in range(i+1, len(permPrimes)-1):
            for k in range(j+1, len(permPrimes)):
                if permPrimes[j] - permPrimes[i] == permPrimes[k] - permPrimes[j]:
                    if permPrimes[i] != permPrimes[j]:
                        print(permPrimes[i], permPrimes[j], permPrimes[k])


if __name__ == "__main__":
    limit = 10**4

    primes = sieve_of_eratosthenes(limit)

    for p in primes:
            checkPrimePermutations(p)
