# Project Euler problem 37: https://projecteuler.net/problem=37
# Author: Tom Harkness
# June 1, 2021

def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while (i*i<=n):
        if n % i == 0:
            return False
        i += 2
    return True

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

def checkLeftToRight(p):
    p = str(p)

    while p != '':
        if not isPrime(int(p)):
            return False
        p = p[1:]
    return True

def checkRightToLeft(p):
    while p != 0:
        if not isPrime(p):
            return False
        p //= 10

    return True

if __name__ == "__main__":
    limit = 10**6
    primes = sieve_of_eratosthenes(limit)

    psum = 0
    count = 0
    # 2, 3, 5, and 7 not included as per question
    for p in primes[4:]:
        if checkLeftToRight(p) and checkRightToLeft(p):
            psum += p
            count += 1
            print(f"found {p}, count: {count}, sum: {psum}")
