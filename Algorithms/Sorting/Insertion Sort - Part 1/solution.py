def arr_to_string(arr):
    string = ""

    for a in arr:
        string += str(a) + " "

    return string.strip()

size = int(input())
arr = [int(temp) for temp in input().split(' ')]
assert(len(arr) == size)

val = arr[-1]
idx = -2

while idx >= -1 * size:
    if arr[idx] > val:
        arr[idx + 1] = arr[idx]
    else:
        break

    idx -= 1
    print(arr_to_string(arr))

arr[idx + 1] = val
print(arr_to_string(arr))
