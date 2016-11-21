N = int(input())
arr = [int(temp) for temp in input().split(' ')]

arr.sort()

out_val = ""
min_distance = 20000001

for i in range(1, N):
    diff = arr[i] - arr[i - 1]
    if diff < min_distance:
        out_val = str(arr[i - 1]) + " " + str(arr[i]) + " "
        min_distance = diff
    elif diff == min_distance:
        out_val += str(arr[i - 1]) + " " + str(arr[i]) + " "

print(out_val.strip())
