def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while (i*i<n):
        if n % i == 0:
            return False
        i += 2
    return True

def isPentagonal(n):
    return (24*n+1)**0.5 % 6 == 5

def primeFactors(n):
    """returns a list of prime factors of n, repeats allowed"""
    pfactors = []

    if n == 1:
        return [1]

    if n == 2:
        return [2]

    if n % 2 == 0:
        while n % 2 == 0:
            n /= 2
            pfactors.append(2)

    i = 3
    while (i*i<n):
        if n % i == 0:
            while n % i == 0:
                n /= i
                pfactors.append(i)
                print(f"n: {n}, i: {i}")
        i += 2
    pfactors.append(int(n))
    return pfactors

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

def getProperDivisors(n):
    if n == 1:
        return [1]

    divisors = [1]

    for i in range(2, n//2+1):
        if n % i == 0:
            divisors.append(i)

    return sorted(divisors)