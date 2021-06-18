# Project Euler problem 124: https://projecteuler.net/problem=124
# Author: Tom Harkness
# June 19, 2021

from math import prod
from operator import itemgetter

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
    while (i*i<=n):
        if n % i == 0:
            pfactors.append(i)
            while n % i == 0:
                n /= i
        i += 2
    pfactors.append(int(n))
    return pfactors

def rad(n):
    return prod(distinctPrimeFactors(n))

if __name__ == "__main__":
    rad_pair_list = []
    for n in range(1,100001):
        rad_pair_list.append((n, rad(n)))

    rad_pair_list.sort(key=itemgetter(1,0))
    print(rad_pair_list[9999][0])