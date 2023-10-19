#!/usr/bin/env python3
'''Each new term in the Fibonacci sequence is generated
   by adding the previous two terms. By starting with
   1 and 2, the first 10 terms will be:

   1,2,3,5,8,13,21,34,55,89,...

   By considering the terms in the Fibonacci sequence
   whose values do not exceed four million, find the
   sum of the even-valued terms.'''
   
import time
num1,num2,sum = 1,1,0
while num1 < 4000000:
    print(num1)
    next_num = num1 + num2
    num1 = num2
    num2 = next_num
    # time.sleep(0.05)
    if (num1%2) == 0:
        sum += num1
print(num1)
print(sum)

    