#!/bin/python3

n = int(input().strip())
A = [int(A_temp) for A_temp in input().strip().split(' ')]
assert(len(A) == n)

history = {}
min_distance = 1000

for i in range(n):
    if A[i] in history:
        min_distance = min(min_distance, i - history[A[i]])

    history[A[i]] = i

print(-1) if min_distance == 1000 else print(min_distance)

