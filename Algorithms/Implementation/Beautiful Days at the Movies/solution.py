i, j, k = [int(temp) for temp in input().split(' ')]

count = 0

for a in range(i, j + 1):
    if (a - int(str(a)[::-1])) % k == 0:
        count += 1

print(count)
