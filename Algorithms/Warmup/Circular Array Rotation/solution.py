#!/bin/python3

n,k,q = [int(temp) for temp in input().strip().split(' ')]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

for a0 in range(q):
    m = int(input().strip())
    
    idx = (m - k) % n
    print(a[idx])

