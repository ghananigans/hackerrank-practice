#!/bin/python3

N = int(input().strip())
B = [int(B_temp) for B_temp in input().strip().split(' ')]

bread = 0
odd = 0

for b in B:
    if b & 1 == 1:
        # Odd
        # Toggle between current status of
        # odd in list
        odd ^= 1

    bread += 2 * odd

print(bread) if odd == 0 else print("NO")
