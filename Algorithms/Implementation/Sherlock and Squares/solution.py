import math

T = int(input())

for t in range(T):
    A, B = [int(temp) for temp in input().split(' ')]
    start = int(math.sqrt(A))

    i = start

    count = 0

    if i ** 2 != A:
        i += 1

    while i ** 2 <= B:
        count += 1
        i += 1

    print(count)
