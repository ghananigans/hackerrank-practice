#!/bin/python3

def int_to_array(val):
    arr = [0] * 10

    for i in range(9, 0, -1):
        mult = 10 ** i
        arr[i] = val // mult
        val = val % mult

    arr[0] = val

    return arr

def solve(val):
    val_list = int_to_array(val)
    count = 0

    for a in val_list:
        if a != 0 and val % a == 0:
            count += 1

    return count

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(solve(n))
