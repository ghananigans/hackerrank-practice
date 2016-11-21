n, d = [int(temp) for temp in input().split(' ')]
arr = [int(temp) for temp in input().split(' ')]
assert(len(arr) == n)

notifications = 0
expenditures = [0] * 201

median_idx1 = (d + 1) // 2
median_idx2 = (d + 2) // 2

for i in range(d):
    expenditures[arr[i]] += 1

for i in range(d, n):
    count = 0
    j = 0
    median1 = -1
    median2 = -1

    while j < 201:
        count += expenditures[j]

        if median1 == -1 and count >= median_idx1:
            median1 = j

        if count >= median_idx2:
            median2 = j
            break

        j += 1

    limit = median1 + median2

    expenditures[arr[i]] += 1
    expenditures[arr[i - d]] -= 1

    if limit <= arr[i]:
        notifications += 1

print(notifications)
