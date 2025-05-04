# Project Euler problem 92: https://projecteuler.net/problem=92
# Author: Tom Harkness
# May 31, 2021

def square_digits(n):
    dsum = 0
    while n != 0:
        dsum += (n%10)**2
        n //=10
    return dsum

def loop_value(n):
    """return whether the square digit chain starting from n loops on 1 or 89"""
    while n not in [1, 89]:
        n = square_digits(n)
    return n

if __name__ == "__main__":
    limit = 10**7
    count = 0
    for n in range(1, limit+1):
        if loop_value(n) == 89:
            count += 1

    print(count)
