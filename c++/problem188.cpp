// Project Euler problem 188: https://projecteuler.net/problem=188
// Author: Tom Harkness
// June 20, 2021

#include <iostream>
#include <cmath>

using namespace std;

typedef long long ll;

ll modpow(ll base, ll exp, ll mod) {
    if (exp == 0) return 1 % mod;
    ll res = modpow(base, exp/2, mod);
    res = (res*res) % mod;
    if (exp % 2 == 1) res = (res*base) % mod;
    return res;
}

ll hyperexp(ll a, ll b, ll mod) {
    if (b == 1) {
        return a;
    }
    ll res = modpow(a,hyperexp(a,b-1,mod),mod);
    return res % mod;
}

int main() {
    ll mod = pow(10,8);
    cout << hyperexp(1777,1855,mod);
}