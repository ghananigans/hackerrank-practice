#!/bin/python3

N = int(input())

stringHistory = [''] * N

for i in range(N):
    stringHistory[i] = input()
    
Q = int(input())

for q in range(Q):
    print(str(stringHistory.count(input())))

