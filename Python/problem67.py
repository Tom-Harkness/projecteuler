# Project Euler problem 67: https://projecteuler.net/problem=67
# Author: Tom Harkness
# May 30, 2021

def collapse_rows(r1, r2):
    """return r1 added with the maximum of the diagonally adjacent numbers of the next row, r2"""
    max_path = [max(r1[i] + r2[i], r1[i] + r2[i+1]) for i in range(len(r1))]
    return max_path


# create triangle and cast to ints
with open("Python/p067_triangle.txt", 'r') as f:
    triangle = [row.strip('\n').split(' ') for row in f.readlines()]

for i in range(len(triangle)):
    triangle[i] = [int(item) for item in triangle[i]]


if __name__ == "__main__":
    # calculate the maximum path from the bottom to the top one row at a time
    rows = len(triangle)
    for i in range(rows-2, -1, -1):
        triangle[i] = collapse_rows(triangle[i], triangle[i+1])

    max_path_sum = triangle[0][0]

    print(max_path_sum)
    