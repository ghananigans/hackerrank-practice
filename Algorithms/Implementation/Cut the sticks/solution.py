#!/bin/python3

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
assert(len(arr) == n)
arr.sort()

i = 0
while i < n:
    print(n - i)
    
    curr_value = arr[i]
    
    while i + 1 < n and arr[i + 1] == curr_value:
        i += 1
   
    i += 1

