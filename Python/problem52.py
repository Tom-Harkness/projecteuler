# Project Euler problem 52: https://projecteuler.net/problem=52
# Author: Tom Harkness
# June 18, 2021

def check_property(n,m):
    return set(str(n)) == set(str(m))

if __name__ == "__main__":
    checked = []
    upper_limit = 1000000
    for n in range(1, upper_limit):
        if n % 1000 == 0:
            print(n)
        if check_property(n,2*n):
            if check_property(n,3*n):
                if check_property(n,4*n):
                    if check_property(n,5*n):
                        if check_property(n,6*n):
                            print(f"found target: {n}")
                            exit()
