#!/usr/bin/env python3

'''A palindromic number reads the same both ways.
   The largest palindrome made from the product
   of two 2-digit numbers is 9009 = 91 x 99.
   Find the largest palindrome made from the
   product of two 3-digit numbers.'''

import math

def reverse(num):
   return int(num != 0) and ((num % 10) *
            (10**int(math.log(num,10))) +
            reverse(num // 10))
num1 = 100
num2 = 100
test = 999666999
while num1 != 1000:
   if (num1 * num2) == reverse(num1 * num2):
      print(True)
   if num1 > num2:
      num2 += 1
print(reverse(test))
