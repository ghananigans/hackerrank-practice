#!/bin/python3

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
arr = [int(a_temp) for a_temp in input().strip().split(' ')]
len_arr = len(arr)
assert(n == len_arr)

moded_arr = [0] * k
for a in arr:
    moded_arr[a % k] += 1

sum = moded_arr[0] * (moded_arr[0] - 1) // 2

for i in range(1, k // 2 + k % 2):
    sum += moded_arr[i] * moded_arr[k - i]

if k % 2 == 0:
    sum += moded_arr[k // 2] * (moded_arr[k // 2] - 1) // 2
    
print(sum)

