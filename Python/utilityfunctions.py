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

def isPentagonal(n):
    return (24*n+1)**0.5 % 6 == 5

def isHexagonal(n):
    return (8*n+1)**0.5 % 4 == 3

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
    while (i*i<=n):
        if n % i == 0:
            while n % i == 0:
                n /= i
                pfactors.append(i)
        i += 2
    if n != 1:
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
    while (i*i<=n):
        if n % i == 0:
            pfactors.append(i)
            while n % i == 0:
                n /= i
        i += 2
    if n != 1:
        pfactors.append(int(n))
    return pfactors

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

def getProperDivisors(n):
    if n == 1:
        return [1]

    divisors = [1]

    for i in range(2, n//2+1):
        if n % i == 0:
            divisors.append(i)

    return sorted(divisors)

def numberOfDivisors(n):
    pFactors = primeFactors(n)
    factor_exponent_pairs = []
    for unique_prime in set(pFactors):
        factor_exponent_pairs.append((unique_prime, pFactors.count(unique_prime)))

    divisors = 1
    for pair in factor_exponent_pairs:
        divisors *= pair[1]+1
    
    return divisors

def properDivisorSum(n):
    if n == 1:
        return 1

    divisor_sum = 1

    for i in range(2, n//2+1):
        if n % i == 0:
            divisor_sum += i

    return divisor_sum

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a

def digit_sum(n):
    dsum = 0
    while n != 0:
        dsum += n % 10
        n //= 10
    return dsum