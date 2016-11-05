#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

total_sum = 0 #total_sum = sum(arr)

for a in arr:
    total_sum += a

print(total_sum)

