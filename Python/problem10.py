# Project Euler problem 10: https://projecteuler.net/problem=10
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
    sum = 0
    for n in range(1, 2*10**6):
        if isPrime(n):
            sum += n
    print(sum)