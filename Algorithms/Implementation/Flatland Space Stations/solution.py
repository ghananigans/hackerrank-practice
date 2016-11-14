#!/bin/python3

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]
assert(len(c) == m)

c.sort()
max_val = c[0]

for i in range(0, m - 1):
    max_val = max((c[i + 1] - c[i]) // 2, max_val)

max_val = max((n - 1) - c[-1], max_val)
print(max_val)
