#!/bin/python3

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

plus = 0
minus = 0
zero = 0

for a in arr:
    if a == 0:
        zero += 1
    elif a > 0:
        plus += 1
    else:
        minus += 1

print("%.6f" % (plus / n))
print("%.6f" % (minus / n))
print("%.6f" % (zero / n))

