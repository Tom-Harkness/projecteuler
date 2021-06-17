# Project Euler problem 31: https://projecteuler.net/problem=31
# Author: Tom Harkness
# June 18, 2021

if __name__ == "__main__":
    currency = [1, 2, 5, 10, 20, 50, 100, 200]
    target = 200
    matching_sums = 0
    for a in range(201):
        print(a)
        coin_sum = a
        if coin_sum > 200:
            continue
        for b in range(101):
            coin_sum = a + 2*b
            if coin_sum > 200:
                continue           
            for c in range(41):
                coin_sum = a + 2*b + 5*c
                if coin_sum > 200:
                    continue  
                for d in range(21):
                    coin_sum = a + 2*b + 5*c + 10*d
                    if coin_sum > 200:
                        continue  
                    for e in range(11):
                        coin_sum = a + 2*b + 5*c + 10*d + 20*e
                        if coin_sum > 200:
                            continue  
                        for f in range(5):
                            coin_sum = a + 2*b + 5*c + 10*d + 20*e + 50*f
                            if coin_sum > 200:
                                continue 
                            for g in range(3):
                                coin_sum = a + 2*b + 5*c + 10*d + 20*e + 50*f + 100*g
                                if coin_sum > 200:
                                    continue 
                                for h in range(2):
                                    coin_sum = a + 2*b + 5*c + 10*d + 20*e + 50*f + 100*g + 200*h
                                    if coin_sum == 200:
                                        matching_sums += 1
                                    if coin_sum > 200:
                                        continue 
    print(matching_sums)
