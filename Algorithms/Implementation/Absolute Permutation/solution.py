#!/bin/python3

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    output = ""

    if k == 0:
        # Difference must be zero so just print in order
        for i in range(1, n + 1):
            output += str(i) + " "

        print(output[:-1])
    elif n % (2 * k) == 0:
        # With array 1, 2, ... N, swap first k values with next k
        # values. Repeat this with next group of 2 * k values until end
        diff = n // k
        step_val = 2 * k

        for i in range(n // step_val):
            first = i * step_val + 1
            last = (i + 1) * step_val + 1
            mid = (first + last) // 2

            for j in range(mid, last):
                output += str(j) + " "

            for j in range(first, mid):
                output += str(j) + " "

        print(output[:-1])
    else:
        # Not possible
        print(-1)
