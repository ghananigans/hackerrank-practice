T = int(input())

for t in range(T):
    N, M, S = [int(temp) for temp in input().split(' ')]
    print((((S - 2) + M) % N) + 1)

