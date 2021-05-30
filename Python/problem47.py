# Project Euler problem 47: https://projecteuler.net/problem=47
# Author: Tom Harkness
# May 30, 2021

def distinctPrimeFactors(n):
    """returns a list of distinct prime factors of n"""
    pfactors = []

    if n == 1:
        return []

    if n == 2:
        return [2]

    if n % 2 == 0:
        pfactors.append(2)
        while n % 2 == 0:
            n /= 2

    i = 3
    while (i*i<n):
        if n % i == 0:
            pfactors.append(i)
            while n % i == 0:
                n /= i
        i += 2
    pfactors.append(int(n))
    return pfactors

if __name__ == "__main__":
    distinct_pfactors_target = 4

    n = 1
    while True:
        run = 0
        for m in range(distinct_pfactors_target):
            if len(distinctPrimeFactors(n+m)) == distinct_pfactors_target:
                run += 1
        if run == distinct_pfactors_target:
            print(n)
            exit()
        run = 0
        n += 1
    