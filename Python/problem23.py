# Project Euler problem 23: https://projecteuler.net/problem=23
# Author: Tom Harkness
# May 31, 2021

from itertools import combinations_with_replacement

def getProperDivisors(n):
    if n == 1:
        return [1]

    divisors = [1]

    for i in range(2, n//2+1):
        if n % i == 0:
            divisors.append(i)

    return sorted(divisors)

def isAbundant(n):
    return sum(getProperDivisors(n)) > n

if __name__ == "__main__":
    smallest_abundant = 1
    limit = 28123
    unwritten_integers = [True]*(limit+1)

    abundant_numbers = [n for n in range(smallest_abundant, limit+1) if isAbundant(n)]
    abundant_pairs = list(combinations_with_replacement(abundant_numbers, 2))
    abundant_sums = list(map(sum, abundant_pairs))
    #for i in range(len(unwritten_integers)):
    #    unwritten_integers[i] = False
    for s in abundant_sums:
        try:
            unwritten_integers[s] = False
        except IndexError:
            pass
    
    unwritten_integers = [_ for _ in range(len(unwritten_integers)) if unwritten_integers[_]]
    answer = sum(unwritten_integers)
    print(answer)
