#!/bin/python3

x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

# x1 + j * v1 = x2 + j * v2
# x1 - x2 = j * (v2 - v1)
# (x1 - x2) / (v2 - v1) = j

if v2 == v1 and x1 != x2:
    print("NO")
elif (x1 - x2) % (v2 - v1) == 0 and (x1 - x2) // (v2 - v1) >= 0:
    print("YES")  
else:
    print("NO")

