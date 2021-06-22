// Project Euler problem 145: https://projecteuler.net/problem=145
// Author: Tom Harkness
// June 23, 2021

#include <iostream>
#include <cmath>
#include <vector>
#include <numeric>

using namespace std;

bool all_odd_digits(int n) {
    while (n != 0) {
        if (n % 2 == 0) {
            return false;
        }
        n /= 10;
    }
    return true;
}

int reverse(int n) {
    int res = 0;
    while (n != 0) {
        res *= 10;
        res += n % 10;
        n /= 10;
    }
    return res;
}

int main () {
    int limit = 1e9;
    int reversible_count = 0;
    for (int i = 0; i < limit; i++) {
        if (i % 10 == 0) {
            continue;
        }
        if (all_odd_digits(i + reverse(i))) {
            reversible_count += 1;
        }
    }
    cout << reversible_count << endl;
}