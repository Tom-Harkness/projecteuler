# Project Euler problem 63: https://projecteuler.net/problem=63
# Author: Tom Harkness
# May 31, 2021


def digit_length(n):
    return len(str(n))

if __name__ == "__main__":
    count = 0
    for base in range(1,10000):
        for exp in range(1,200 ):
            if digit_length(base**exp) == exp:
                print(f"{base} ** {exp} == {base**exp}")
                count += 1
    
    print(f"Count: {count}")
