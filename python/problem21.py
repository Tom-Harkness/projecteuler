# Project Euler problem 21: https://projecteuler.net/problem=21
# Author: Tom Harkness
# May 29, 2021


def getProperDivisors(n):
    if n == 1:
        return [1]

    divisors = [1]

    for i in range(2, n//2+1):
        if n % i == 0:
            divisors.append(i)

    return sorted(divisors)

def d(n):
    return sum(getProperDivisors(n))

if __name__ == "__main__":
    amicable = []
    for i in range(2,10000):
        divsum = d(i)
        if divsum > 1 and divsum != i:
            if i == d(divsum):
                amicable.append(i)
                print(i)
    print(sum(amicable))