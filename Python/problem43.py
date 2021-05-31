# Project Euler problem 43: https://projecteuler.net/problem=43
# Author: Tom Harkness
# June 1, 2021

from itertools import permutations

def getPandigitals():
    digits = '0123456789'
    pandigitals = [''.join(_) for _ in permutations(digits) if not _[0] == '0']
    return pandigitals

def checkProperty(n):
    for i in range(7):
        if not int(n[i+1:i+4]) % primes[i] == 0:
            return False
    return True


if __name__ == "__main__":
    pandigitals = getPandigitals()
    primes = [2,3, 5, 7, 11, 13, 17]

    answer = 0
    for p in pandigitals:
        if checkProperty(p):
            answer += int(p)
    print(answer)
