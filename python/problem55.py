# Project Euler problem 55: https://projecteuler.net/problem=55
# Author: Tom Harkness
# June 17, 2021

def isPalindrome(n):
    return str(n)[::-1] == str(n)

def reverseAndAdd(n):
    rev = int(str(n)[::-1])
    return n + rev

def isLychrel(n):
    iterations = 1
    n = reverseAndAdd(n)
    while not isPalindrome(n):
        n = reverseAndAdd(n)
        iterations += 1
        if iterations > 51:
            return True
    return False
    

if __name__ == "__main__":
    count = 0
    for n in range(1, 10000):
        print(n)
        if isLychrel(n):
            count += 1
    print(count)
