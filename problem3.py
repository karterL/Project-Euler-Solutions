#!/usr/bin/env python3
def prime_list():
    primes = [2]
    num = 3
    while num < 1000:
        for i in range(2,num):
            if (num%i) == 0:
                break
            elif (num-1) == i:
                primes.append(num)
        num += 1
    return primes

def prime_factor(num, primes):
    for i in range(len(primes)):
        if (num%primes[i]) == 0:
            qualified_primes.append(primes[i])
            num = num/primes[i]
            print(primes[i])


primes = prime_list()
print(primes)
num = 600851475143
qualified_primes = []
prime_factor(num, primes)

