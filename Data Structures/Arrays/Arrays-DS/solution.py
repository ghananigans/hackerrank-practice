#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

stringOut = ""

for a in arr:
    stringOut = str(a) + " " + stringOut
    
print(stringOut)

