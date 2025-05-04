# Project Euler problem 179: https://projecteuler.net/problem=179
# Author: Tom Harkness
# June 19, 2021

def primeFactors(n):
    """returns a list of prime factors of n, repeats allowed"""
    pfactors = []

    if n == 1:
        return [1]
    if n == 2:
        return [2]
    if n % 2 == 0:
        while n % 2 == 0:
            n /= 2
            pfactors.append(2)
    i = 3
    while (i*i<=n):
        if n % i == 0:
            while n % i == 0:
                n /= i
                pfactors.append(i)
        i += 2
    if n != 1:
        pfactors.append(int(n))
    return pfactors


def numberOfDivisors(n):
    pFactors = primeFactors(n)
    factor_exponent_pairs = []
    for unique_prime in set(pFactors):
        factor_exponent_pairs.append((unique_prime, pFactors.count(unique_prime)))

    divisors = 1
    for pair in factor_exponent_pairs:
        divisors *= pair[1]+1
    
    return divisors


if __name__ == "__main__":
    count = 0
    current = numberOfDivisors(2)
    n = 3
    while n < 10**7:
        if n % 100 == 0:
            print(n)
        next = numberOfDivisors(n)
        if current == next:
            count += 1
        n += 1
        current = next
    print(count)
        