#!/bin/python3

import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
    
sum = -100
for i in range(2, len(arr)):
    for j in range (2, len(arr[i])):
        temp_sum = arr[i - 2][j - 2] # Top Left
        temp_sum += arr[i][j - 2] # Bottom Left
        temp_sum += arr[i - 2][j - 1] # Top Middle
        temp_sum += arr[i - 1][j - 1] # Middle Middle
        temp_sum += arr[i][j - 1] # Bottom Middle
        temp_sum += arr[i - 2][j] # Top Right
        temp_sum += arr[i][j] # Bottom Right
        
        sum = max(sum, temp_sum)
        
print(str(sum))
