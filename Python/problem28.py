# Project Euler problem 28: https://projecteuler.net/problem=28
# Author: Tom Harkness
# May 31, 2021

def layer_value(layer):
    # layer 1 is 1
    # layer 2 is bounded by 3, 5, 7, 9, etc
    # the top right corner of layer n is (2n-1)**2
    # layer_increment is the difference between successive corners of a layer
    # total layer value is 4*(2n-1)**2 - 6*layer_increment
    if layer == 1: 
        return 1
    layer_increment = 2*layer-2
    return 4*(2*layer-1)**2 - 6*layer_increment

def spiral_diagonal_sum(spiral_size):
    num_layers = (spiral_size+1)//2

    diagonal_sum = 0
    for l in range(1, num_layers+1):
        diagonal_sum += layer_value(l)

    return diagonal_sum

if __name__ == "__main__":
    print(spiral_diagonal_sum(1001))
