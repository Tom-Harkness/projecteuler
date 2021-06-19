# Project Euler problem 187: https://projecteuler.net/problem=187
# Author: Tom Harkness
# June 20, 2021

def sieve_of_eratosthenes(limit):
    """returns a list of the primes under `limit`"""
    numbers = [False]*2 + (limit-1)*[True]

    n = 2
    while n*n <= limit:
        if numbers[n]:
            m = n*n
            while m <= limit:
                numbers[m] = False
                m += n
        n += 1
    return sorted([_ for _ in range(len(numbers)) if numbers[_]])

if __name__ == "__main__":
    primes = sieve_of_eratosthenes(5*10**7)
    products = set()
    prod = 0

    for p in primes:
        for q in primes:
            prod = p*q
            if prod >= 10**8:
                prod = 0
                break
            else:
                products.update([prod])

    print(f"answer:{len(products)}")