N, M = [int(temp) for temp in input().split(' ')]

array_N = [0] * (N + 1)

for b in range(M):
    a, b, k = [int(temp) for temp in input().split(' ')]
    array_N[a - 1] += k
    array_N[b] -= k

sum = 0
for n in range(N):
    sum += array_N[n]
    array_N[n] = sum

print(max(array_N))
