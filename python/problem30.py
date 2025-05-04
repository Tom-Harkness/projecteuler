# Project Euler problem 30: https://projecteuler.net/problem=30
# Author: Tom Harkness
# June 17, 2021

def digit_power_sum(n, power):
    dsum = 0
    while n != 0:
        dsum += (n % 10)**power
        n //= 10
    return dsum

if __name__ == "__main__":
    # upper limit is 354294 = 6*9**5, 7*9**5 is only 6 digits
    upper_limit = 355000
    power = 5
    matching_numbers = []
    for n in range(2, upper_limit):
        if digit_power_sum(n, power) == n:
            matching_numbers.append(n)

    print(sum(matching_numbers))
    


