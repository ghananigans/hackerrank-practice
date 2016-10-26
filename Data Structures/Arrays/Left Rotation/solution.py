#!/bin/python3

n, d = [int(temp) for temp in input().split(' ')]
arr = [int(temp) for temp in input().split(' ')]
d = d % n
arr = arr[d:] + arr[:d]

for a in arr[:-1]:
    print(str(a) + " ", end="")
    
print(str(arr[-1]))

