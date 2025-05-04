# Project Euler problem 3: https://projecteuler.net/problem=3
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
    input = 600851475143
    print(max(primeFactors(input)))