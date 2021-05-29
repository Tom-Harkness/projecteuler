# Project Euler problem 22: https://projecteuler.net/problem=22
# Author: Tom Harkness
# May 29, 2021

def score_name(name, position):
    sum = 0
    for c in name.lower():
        sum += letter_dict[c]
    
    return sum*position

letter_dict = {}
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in range(1,27):
    letter_dict[alphabet[i-1]] = i

if __name__ == "__main__":
    with open("Python/p022_names.txt", 'r') as f:
        names = f.readlines()[0].split(',')

    names = sorted([n.strip('"') for n in names])

    total_sum = 0
    for i in range(len(names)):
        total_sum += score_name(names[i], i+1)

    print(total_sum)