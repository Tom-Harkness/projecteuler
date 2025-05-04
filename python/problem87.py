# Project Euler problem 87: https://projecteuler.net/problem=87
# Author: Tom Harkness
# June 18, 2021

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
    primes = sieve_of_eratosthenes(8000)
    sums = []
    limit = 50*10**6
    for p in primes:
        print(p)
        res = p**2
        if res >= limit:
            continue
        for q in primes:
            res = p**2 + q**3
            if res >= limit:
                continue
            for r in primes:
                res = p**2 + q**3 + r**4
                if res >= limit:
                    continue
                if res not in sums:
                    #print(f"{res} = {p}**2 + {q}**3 + {r}**4")
                    sums.append(res)
    print(f"answer: {len(sums)}")
