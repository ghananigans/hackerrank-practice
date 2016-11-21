n = int(input())
arr = [int(temp) for temp in input().split(' ')]
assert(len(arr) == n)
arr.sort()

print(arr[n // 2])
