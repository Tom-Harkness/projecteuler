# Project Euler problem 45: https://projecteuler.net/problem=45
# Author: Tom Harkness
# June 1, 2021

def isPentagonal(n):
    return (24*n+1)**0.5 % 6 == 5

def isHexagonal(n):
    return (8*n+1)**0.5 % 4 == 3

def triangle(n):
    return n*(n+1)//2

if __name__ == "__main__":
    n = 2
    count = 0
    while count < 2:
        t_n = triangle(n)
        if isPentagonal(t_n):
            if isHexagonal(t_n):
                print(t_n)
                count += 1
        n += 1
