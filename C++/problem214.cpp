// Project Euler problem 214: https://projecteuler.net/problem=214
// Author: Tom Harkness
// July 1, 2021

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;

vector<ll> sieve_of_eratosthenes(ll n) {
    vector<int> sieve(n+1,0);
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

vector<ll> primeFactors(ll n) {
    vector<ll> pFactors;

    if (n % 2 == 0) {
        while (n % 2 == 0) {
            n /= 2;
            pFactors.push_back(2);
        }
    }
    
    for (ll i = 3; i*i <= n; i += 2) {
        if (n % i == 0) {
            while (n % i == 0) {
                n /= i;
                pFactors.push_back(i);
            }
        }
    }
    if (n != 1) {
        pFactors.push_back(n);
    }
    return pFactors;
}

ll pow(ll base, ll exp) {
    if (exp == 0) return 1;
    ll res = pow(base, exp/2);
    res = (res*res);
    if (exp % 2 == 1) res = (res*base);
    return res;
}

ll phi(ll n) {
    vector<ll> pFactors = primeFactors(n);
    ll res = 1;
    for (auto p : pFactors) {
        int p_k = count(pFactors.begin(), pFactors.end(), p);

        if (res % p != 0) {
            res *= pow(p, p_k - 1)*(p-1);
        }
    }
    return res;
}

bool scanChain(ll n) {
    // return true if totient chain has length 25, otherwise false"""
    int chain_length = 1;
    while (true) {
        n = phi(n);
        chain_length += 1;
        if (chain_length > 25) {
            return false;
        }
        if (n == 1) {
            if (chain_length == 25) {
                return true;
            }
            return false;
        }
    }
}

int main() {
    ll answer = 0;
    ll limit = 4e7;
    vector<ll> primes = sieve_of_eratosthenes(limit);
    for (auto p : primes) {
        cout << p << endl;
        if (scanChain(p)) {
            answer += p;
        }
    }
    cout << answer << endl;
}