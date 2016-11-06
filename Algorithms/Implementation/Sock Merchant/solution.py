#!/bin/python3

n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
arr = [0] * 101

for i in c:
    arr[i] += 1

sum = 0

for i in arr:
    sum += i // 2

print(sum)

