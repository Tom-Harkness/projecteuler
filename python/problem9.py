# Project Euler problem 9: https://projecteuler.net/problem=9
# Author: Tom Harkness
# May 29, 2021

if __name__ == "__main__":
    for a in range(1,800):
        for b in range(a,800):
            for c in range(b,800):
                if a + b + c == 1000:
                    if a**2 + b**2 == c**2:
                        print(a*b*c)
                        exit()