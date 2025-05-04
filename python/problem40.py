# Project Euler problem 40: https://projecteuler.net/problem=40
# Author: Tom Harkness
# June 17, 2021

def generateChampernowne(digit_limit):
    current_length = 0
    champ_decimal = ""
    n = 1
    while current_length <= digit_limit:
        champ_decimal += str(n)
        current_length += len(str(n))
        n += 1
    return champ_decimal[:digit_limit]

def d(n):
    return int(generateChampernowne(n+2)[n-1])

if __name__ == "__main__":
    answer = 1
    for n in range(1,7):
        answer *= d(10**n)
    print(answer)
