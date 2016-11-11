#!/bin/python3

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]
assert(len(c) == n)

pos = 0
E = 100

pos = (pos + k) % n
while pos != 0:
    E -= 1

    if c[pos] == 1:
        E -= 2

    pos = (pos + k) % n

if c[pos] == 1:
    E -= 3
else:
    E -= 1

print(E)
