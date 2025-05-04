# Project Euler problem 80: https://projecteuler.net/problem=80
# Author: Tom Harkness
# June 19, 2021

from decimal import Decimal, getcontext

def digit_sum(n):
    dsum = 0
    while n != 0:
        dsum += n % 10
        n //= 10
    return dsum

if __name__ == "__main__":
    getcontext().prec = 250
    total_sum = 0
    for n in range(2,101):
        if n**0.5 % 1 != 0:
            s = str(Decimal(n).sqrt())
            s = s.replace('.','')
            s = s[:100]
            total_sum += digit_sum(int(s))

    print(total_sum)
