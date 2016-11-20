def quicksort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    left = []
    right = []

    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        elif arr[i] > pivot:
            right.append(arr[i])

    left = quicksort(left)
    right = quicksort(right)

    arr = left + [pivot] + right

    print(" ".join(map(str, arr)))
    return(arr)

n = int(input())
ar = [int(temp) for temp in input().split(' ')]
assert(len(ar) == n)
quicksort(ar)
