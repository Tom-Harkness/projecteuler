# Project Euler problem 69: https://projecteuler.net/problem=69
# Author: Tom Harkness
# June 18, 2021


def primeFactors(n):
    """returns a list of prime factors of n, repeats allowed"""
    pfactors = []
    if n == 1:
        return [1]

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
                n /= i
                pfactors.append(i)
        i += 2
    if n != 1:
        pfactors.append(n)
    return pfactors


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


def phi(n):
    pfactors = primeFactors(n)
    result = 1
    for p in set(pfactors):
        exp = pfactors.count(p)
        result *= p**(exp-1)*(p-1)
    return result


if __name__ == "__main__":
    primes = sieve_of_eratosthenes(10**7)
    best_n = 0
    best_fraction = 0
    for n in range(2,10**6+1):
        f = n/phi(n)
        if f > best_fraction:
            best_n = n
            best_fraction = f
            print(n, f)
    print(best_n)
