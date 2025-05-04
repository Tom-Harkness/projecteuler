# Project Euler problem 7: https://projecteuler.net/problem=7
# Author: Tom Harkness
# May 29, 2021

def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n**0.5+1), 2):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    primeCount = 0
    i = 1
     
    while True:
        if isPrime(i):
            primeCount += 1
        if primeCount == 10001:
            print(i)
            break
        i += 1
