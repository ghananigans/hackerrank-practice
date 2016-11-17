#!/bin/python

vals = [int(temp) for temp in input().split(' ')]
assert(len(vals) == 5)

total = sum(vals)
min_val = total - vals[0]
max_val = total - vals[0]

for i in range(1, 5):
    max_val = max(max_val, total - vals[i])
    min_val = min(min_val, total - vals[i])

print(str(min_val) + " " + str(max_val))
