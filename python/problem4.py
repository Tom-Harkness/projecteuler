# Project Euler problem 4: https://projecteuler.net/problem=4
# Author: Tom Harkness
# May 29, 2021

if __name__ == "__main__":
    best = 0
    for i in range(1, 1000):
        for j in range(1, 1000):
            s = i*j
            if s> best:
                if str(s) == str(s)[::-1]:
                    best = s
    print(best)