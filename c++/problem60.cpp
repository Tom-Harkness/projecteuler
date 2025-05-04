// Project Euler problem 60: https://projecteuler.net/problem=60
// Author: Tom Harkness
// June 23, 2021

#include <iostream>
#include <cmath>
#include <vector>
#include <numeric>
#include <algorithm>
#include <set>
#include <string>

using namespace std;

typedef long long ll;

vector<ll> sieve_of_eratosthenes(ll n) {
    vector<ll> sieve(n+1,0);
    vector<ll> primes;

    for (ll i = 2; i <= n; i++) {
        if (sieve[i]) continue;
        primes.push_back(i);
        for (ll j = 2*i; j <= n; j += i) {
            sieve[j] = 1;
        }
    }
    return primes;
}

bool isPrime(ll n) {
    if (n == 1) {
        return false;
    }
    if (n == 2) {
        return true;
    }
    if (n % 2 == 0) {
        return false;
    }
    for (ll i = 3; i*i <= n; i += 2) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int prime_pairs(int p1, int p2, int p3, int p4, int p5) {
    string s1 = to_string(p1);
    string s2 = to_string(p2);
    string s3 = to_string(p3);
    string s4 = to_string(p4);
    string s5 = to_string(p5);
    vector<string> p_strings = {s1, s2, s3, s4, s5};

    int count = 0;
    string s;
    ll sll;
    for (int i = 0; i < p_strings.size(); i++) {
        for (int j = 0; j < p_strings.size(); j++) {
            if (i == j) {
                continue;
            }
            s = p_strings[i] + p_strings[j];
            sll = stoll(s);
            if (isPrime(sll)) {
                count += 1;
            }
        }
    }
    return count;
}

ll concat(int n1, int n2) {
    string s1 = to_string(n1);
    string s2 = to_string(n2);
    return stoll(s1+s2);
}

int main() {
    vector<ll> primes;
    ll limit = 10000;
    primes = sieve_of_eratosthenes(limit);
    int set_size = 5;
    int concat_combinations = set_size*(set_size-1);

    int pcount;
    int lowest_sum = 1e9;
    int set_sum;
    for (int i1 = 0; i1 < primes.size()-3; i1++) {
        for (int i2 = i1+1; i2 < primes.size()-2; i2++) {
            if (isPrime(concat(primes[i1], primes[i2])) &&
                isPrime(concat(primes[i2], primes[i1]))) {
                for (int i3 = i2+1; i3 < primes.size()-1; i3++) {
                    if (isPrime(concat(primes[i1], primes[i3])) && 
                        isPrime(concat(primes[i3], primes[i1])) && 
                        isPrime(concat(primes[i2], primes[i3])) &&
                        isPrime(concat(primes[i3], primes[i2]))) {
                        for (int i4 = i3+1; i4 < primes.size(); i4++) {
                            if (isPrime(concat(primes[i1], primes[i4])) &&
                                isPrime(concat(primes[i4], primes[i1])) &&  
                                isPrime(concat(primes[i2], primes[i4])) &&
                                isPrime(concat(primes[i4], primes[i2])) && 
                                isPrime(concat(primes[i3], primes[i4])) &&  
                                isPrime(concat(primes[i4], primes[i3]))) {
                                for (int i5 = i4+1; i5 < primes.size(); i5++) {
                                    if (isPrime(concat(primes[i1], primes[i5])) &&
                                        isPrime(concat(primes[i2], primes[i5])) &&
                                        isPrime(concat(primes[i3], primes[i5])) &&
                                        isPrime(concat(primes[i4], primes[i5])) &&
                                        isPrime(concat(primes[i5], primes[i4])) &&
                                        isPrime(concat(primes[i5], primes[i3])) &&
                                        isPrime(concat(primes[i5], primes[i2])) &&
                                        isPrime(concat(primes[i5], primes[i1]))) {
                                        cout << primes[i1] << " " << primes[i2]  << " " << primes[i3] << " " << primes[i4] << " " << primes[i5] << endl;
                                        pcount = prime_pairs(primes[i1], primes[i2], primes[i3], primes[i4], primes[i5]);
                                        if (pcount == concat_combinations) {
                                            cout << primes[i1] << " " << primes[i2] << " " << primes[i3] << " " << primes[i4] << " " << primes[i5] << endl;
                                            set_sum = primes[i1] + primes[i2] + primes[i3] + primes[i4] + primes[i5];
                                            if (set_sum < lowest_sum) {
                                                lowest_sum = set_sum;
                                                cout << "new lowest set sum: " << lowest_sum << endl;
                                            }
                                        }
                                    }     
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    cout << lowest_sum << endl;
    return 0;
}