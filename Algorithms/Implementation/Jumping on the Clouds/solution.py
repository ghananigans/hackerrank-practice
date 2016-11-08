#!/bin/python3

n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
assert(len(c) == n)

count = 0
cloud = 0

while cloud != n - 1:
    if cloud + 2 < n and c[cloud + 2] == 0:
        cloud = cloud + 2
    else:
        cloud = cloud + 1
    
    count += 1

print(count)

