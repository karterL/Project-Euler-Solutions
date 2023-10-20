#!/usr/bin/env python3

'''The prime factors of 13195 are 5, 7, 13, and 29.
   What is the largest prime factor of the number
   600851475143?'''

num = 600851475143
prime = 3
while True:
    for i in range(2, prime):
        if (prime%i) == 0:
            break
        elif ((prime-1) == i) and ((num%prime) == 0):
            num = num//prime
            print(num, prime)
    if num == 1:
        break
    prime += 1
print("The largest prime factor is ",prime)


