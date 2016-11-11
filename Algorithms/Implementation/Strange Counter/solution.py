#!/bin/python3

t = int(input().strip())
val = 3

current_t = 1
while current_t + val <= t:
    current_t += val
    val = val << 1

val -= t - current_t
print(val)

