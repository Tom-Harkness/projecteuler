# Project Euler problem 46: https://projecteuler.net/problem=46
# Author: Tom Harkness
# June 20, 2021

def isPrime(n):
    if n == 1:
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

if __name__ == "__main__":
    primes = sieve_of_eratosthenes(10**5)
    squares = [_**2 for _ in range(1,10001)]
    sum_results = set()
    for p in primes:
        print(p)
        for s in squares:
            sum_results.update([p+2*s])
    sum_results = sorted(list(sum_results))
    
    n = 9
    while True:
        if not isPrime(n):
            if not n in sum_results:
                print(f"answer: {n}")
                exit()
        n += 2
