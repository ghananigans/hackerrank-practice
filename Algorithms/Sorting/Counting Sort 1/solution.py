n = int(input())
arr = [int(temp) for temp in input().split(' ')]

counter = [0] * 100

for a in arr:
    counter[a] += 1

print(" ".join(map(str, counter)))
