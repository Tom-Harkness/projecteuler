# Project Euler problem 36: https://projecteuler.net/problem=36
# Author: Tom Harkness
# May 31, 2021

def isPalindrome_10(n):
    return str(n) == str(n)[::-1]

def isPalindrome_2(n):
    s = bin(n)[2:]
    return s == s[::-1]

if __name__ == "__main__":
    limit = 1000000
    total_sum = 0
    for n in range(1, limit):
        if isPalindrome_10(n) and isPalindrome_2(n):
            total_sum += n
    print(total_sum)