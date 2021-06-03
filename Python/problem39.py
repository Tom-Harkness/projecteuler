# Project Euler problem 39: https://projecteuler.net/problem=39
# Author: Tom Harkness
# June 3, 2021

if __name__ == "__main__":
    perimeter_counts = dict([(p, 0) for p in range(12, 2000)])
    
    for a in range(2, 400):
        for b in range(a, 450):
            c = (a*a + b*b)**0.5 
            if c % 1 == 0:
                perimeter_counts[round(a + b + c)] += 1

    print(max(perimeter_counts, key=perimeter_counts.get))
