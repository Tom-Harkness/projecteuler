# Project Euler problem 12: https://projecteuler.net/problem=12
# Author: Tom Harkness
# May 31, 2021

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
    while (i*i<n):
        if n % i == 0:
            while n % i == 0:
                n /= i
                pfactors.append(i)
        i += 2
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
    divisor_target = 500
    best = 0
    triangle_n = 1
    increment = 2

    while best < divisor_target:
        #print(triangle_n)
        triangle_n += increment
        increment += 1
        divs = numberOfDivisors(triangle_n)
        if divs > best:
            print(f"new best: {triangle_n} has {divs} divisors")
            best = divs
