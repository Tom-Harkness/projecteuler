# Project Euler problem 5: https://projecteuler.net/problem=5
# Author: Tom Harkness
# May 29, 2021

def primeFactors(n):
    """returns a list of prime factors of n, repeats allowed"""
    pfactors = []
    n_original = n
    if n == 1:
        return [1]

    if n == 2:
        return [2]

    if n % 2 == 0:
        while n % 2 == 0:
            n //= 2
            pfactors.append(2)

    i = 3
    while True:
        if n % i == 0:
            while n % i == 0:
                n //= i
                pfactors.append(i)
        if (i*i >= n_original):
            break
        i += 2

    if pfactors == []:
        return [n_original]

    return pfactors

if __name__ == "__main__":
    unique_prime_factors = []
    max_factor_counts = {}
    for i in range(1,20):
        factors = primeFactors(i)
        for p in factors:
            if p not in max_factor_counts:
                max_factor_counts[p] = factors.count(p)
            elif factors.count(p) > max_factor_counts[p]:
                max_factor_counts[p] = factors.count(p)
    print(max_factor_counts)

    result = 1
    for k, v in max_factor_counts.items():
       result *= k**v
    print(result)
