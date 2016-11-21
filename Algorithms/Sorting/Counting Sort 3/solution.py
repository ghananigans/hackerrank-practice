n = int(input())
arr = [0] * n

for i in range(n):
    arr[i] = input().split(' ')
    arr[i] = int(arr[i][0])

counter = [0] * 100
out_str = ""

for a in arr:
    counter[a] += 1

for i in range(1, 100):
    counter[i] += counter[i - 1]

print(" ".join(map(str, counter)))
