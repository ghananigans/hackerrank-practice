#!/bin/python3

a = [int(temp) for temp in input().strip().split(' ')]
b = [int(temp) for temp in input().strip().split(' ')]

assert(len(a) == 3)
assert(len(b) == 3)

alice_points = 0
bob_points = 0

for i in range(3):
    if a[i] > b[i]:
        alice_points += 1
    elif b[i] > a[i]:
        bob_points += 1

print(str(alice_points) + " " + str(bob_points))

