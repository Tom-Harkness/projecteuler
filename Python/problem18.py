# Project Euler problem 18: https://projecteuler.net/problem=18
# Author: Tom Harkness
# May 30, 2021

def collapse_rows(r1, r2):
    """return r1 added with the maximum of the diagonally adjacent numbers of the next row, r2"""
    max_path = [max(r1[i] + r2[i], r1[i] + r2[i+1]) for i in range(len(r1))]
    return max_path


# create triangle and cast to ints
triangle_string = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

triangle = triangle_string.split("\n")[1:]
for i in range(len(triangle)):
    triangle[i] = [int(item) for item in triangle[i].split(' ')]


if __name__ == "__main__":
    # calculate the maximum path from the bottom to the top one row at a time
    rows = len(triangle)
    for i in range(rows-2, -1, -1):
        triangle[i] = collapse_rows(triangle[i], triangle[i+1])

    max_path_sum = triangle[0][0]

    print(max_path_sum)
    