# Project Euler problem 206: https://projecteuler.net/problem=206
# Author: Tom Harkness
# June 19, 2021

from itertools import product
from math import isqrt

def is_square(n):
    return isqrt(n)**2 == n

def check_concealed_square(digit_list):
    return is_square(int(f"1{d1}2{d2}3{d3}4{d4}5{d5}6{d6}7{d7}8{d8}9{d9}0"))

if __name__ == "__main__":
    for d1 in range(10):
        for d2 in range(10):
            print(d2)
            for d3 in range(10):
                for d4 in range(10):
                    for d5 in range(10):
                        for d6 in range(10):
                            for d7 in range(10):
                                for d8 in range(10):
                                    for d9 in range(10):
                                        num = int(f"1{d1}2{d2}3{d3}4{d4}5{d5}6{d6}7{d7}8{d8}9{d9}0")
                                        if check_concealed_square(num):
                                            print(f"Answer: {int(num**0.5)}")
                                            exit()
