#!/usr/bin/env python3
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

    