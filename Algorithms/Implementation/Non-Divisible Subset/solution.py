#!/bin/python3

n, k = [int(temp) for temp in input().strip().split(' ')]
arr = [int(temp) for temp in input().strip().split(' ')]
assert(len(arr) == n)
    
k_arr = [0] * k

for a in arr:
    k_arr[a % k] += 1

max_subset_size = 0

for i in range(1, (k + 1) // 2):
    j = k - i
    max_subset_size += max(k_arr[i], k_arr[j])

if k % 2 == 0 and k_arr[k // 2] > 0:
    max_subset_size += 1
    
if k_arr[0] > 0:
    max_subset_size += 1
    
print(max_subset_size)

