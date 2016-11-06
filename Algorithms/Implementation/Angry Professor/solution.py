#!/bin/python3

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    
    for time_offset in a:
        if time_offset <= 0:
            k -= 1
            
    if k <= 0:
        print("NO")
    else:
        print("YES")

