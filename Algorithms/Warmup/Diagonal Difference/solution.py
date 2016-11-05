#!/bin/python3

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

assert(len(a) == n)
sum_a = 0
sum_b = 0

for i in range(n):
    assert(len(a[i]) == n)
    
    sum_a += a[i][i]
    sum_b += a[i][n - i - 1]
    
print(abs(sum_a - sum_b))

