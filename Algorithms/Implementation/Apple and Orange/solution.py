#!/bin/python3

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apples = [int(apple_temp) for apple_temp in input().strip().split(' ')]
oranges = [int(orange_temp) for orange_temp in input().strip().split(' ')]

apple_count = 0
orange_count = 0

for d in apples:
    p = a + d
    
    if p >= s and t >= p:
        apple_count += 1
        
for d in oranges:
    p = b + d
    
    if p >= s and t >= p:
        orange_count += 1

print(apple_count)
print(orange_count)

