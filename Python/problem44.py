# Project Euler problem 44: https://projecteuler.net/problem=44
# Author: Tom Harkness
# May 31, 2021


def generatePentagonals(n):
    """return the first `n` pentagonal numbers"""
    return n*(3*n-1)//2

def isPentagonal(n):
    return (24*n+1)**0.5 % 6 == 5

if __name__ == "__main__":
    terms = 10000
    pentagonals = [generatePentagonals(n) for n in range(1,terms+1)]

    pairs = []
    i = 0
    for i in range(len(pentagonals)-1):
        for j in range(i, len(pentagonals)):
    #         #pairs.append((pentagonals[i], pentagonals[j]))
            p_i = pentagonals[i]
            p_j = pentagonals[j]
            if isPentagonal(p_i + p_j):
                if isPentagonal(p_j - p_i):
                    print(p_i, p_j)
                    print(abs(p_i-p_j))
                    exit()