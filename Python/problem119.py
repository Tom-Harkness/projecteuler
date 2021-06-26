# Project Euler problem 119: https://projecteuler.net/problem=119
# Author: Tom Harkness
# June 16, 2021

def digit_sum(n):
    if n < 10:
        return 0
    dsum = 0
    while n != 0:
        dsum += n % 10
        n //= 10
    return dsum


if __name__ == "__main__":
    a = []
    for base in range(2, 10000):
        for exp in range(1, 100):
            res = base**exp
            dsum = digit_sum(res)
            if len(str(res)) > 2:
                if digit_sum(res) == base:
                    print(f"{base}**{exp} -> digitsum: {digit_sum(res)}")
                    a.append(res)
    a = sorted(list(a))
    print(a[28])
