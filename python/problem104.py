# Project Euler problem 104: https://projecteuler.net/problem=104
# Author: Tom Harkness
# June 4, 2021

def first_nine(n):
    f_nine = ''.join(sorted(str(n)[:9]))
    return f_nine == "123456789"

def last_nine(n):
    l_nine = n % 10**9
    return set(str(l_nine)) == set("123456789")

if __name__ == "__main__":
    a, b = 1,1
    k = 2
    while True:
        print(k)
        if last_nine(b):
            if first_nine(b):
                print(k)
                break
        a, b = b, a + b
        k += 1
