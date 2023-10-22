#!/usr/bin/env python3

'''A palindromic number reads the same both ways.
   The largest palindrome made from the product
   of two 2-digit numbers is 9009 = 91 x 99.
   Find the largest palindrome made from the
   product of two 3-digit numbers.'''

palindrome = 0
for i in range(999,100,-1):
   for j in range(i,100,-1):
      print(i,' ',j)
      num = i * j
      if num > palindrome:
         snum = str(i * j)
         if snum == snum[::-1]:
            palindrome = i * j
print(palindrome)
