#!/bin/python3

import sys

num_blocks = [int(temp) for temp in input().strip().split(' ')]

stacks = [None] * 3
stacks[0] = [int(h1_temp) for h1_temp in input().strip().split(' ')]
stacks[1] = [int(h2_temp) for h2_temp in input().strip().split(' ')]
stacks[2] = [int(h3_temp) for h3_temp in input().strip().split(' ')]

for stack in stacks:
    stack.reverse()

heights = [sum(stack) for stack in stacks]

while heights[1:] != heights[:-1]:
    max_height = max(heights)
    i = heights.index(max_height)

    heights[i] -= stacks[i][-1]
    stacks[i].pop()
    
print(heights[0])

