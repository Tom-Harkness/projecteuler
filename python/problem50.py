# Project Euler problem 50: https://projecteuler.net/problem=50
# Author: Tom Harkness
# June 17, 2021

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
    primes = sieve_of_eratosthenes(10**6)
    count = 0
    length_limit = 600
    max_length_found = 0
    max_prime = 0

    p_ind = 0
    while p_ind < len(primes) - length_limit:
        for l in range (20, length_limit):
            subset = primes[p_ind:p_ind+l]
            if sum(subset) in primes:
                if l > max_length_found:
                    print(f"{l=}, {sum(subset)=}, {subset=}")
                    max_length_found = l
                    max_prime = sum(subset)
        p_ind += 1
    
    print(max_prime)
