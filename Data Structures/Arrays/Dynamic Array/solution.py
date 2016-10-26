#!/bin/python3

line = [int(arr_temp) for arr_temp in input().strip().split(' ')]

N = line[0]
Q = line[1]

seqList = [[] for a in range(N)]
lastAns = 0

for i in range(Q):
    arr = [int(temp) for temp in input().strip().split(' ')]
    
    query_type = arr[0]
    x = arr[1]
    y = arr[2]
    seq = (x ^ lastAns) % N
    
    if query_type == 1:
        seqList[seq].append(y)
    elif query_type == 2:
        lastAns = seqList[seq][y % len(seqList[seq])]
        print(str(lastAns))
    else:
        assert(False)

