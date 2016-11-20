def quicksort_partial(arr, start, end):
    if start >= end:
        return

    pivot = arr[end]
    lower_idx = start - 1
    greater = 0

    for i in range(start, end):
        if arr[i] < pivot:
            lower_idx += 1

            if greater > 0:
                arr[lower_idx], arr[i] = arr[i], arr[lower_idx]
                greater -= 1

        if arr[i] > pivot:
            greater += 1

    arr[end], arr[lower_idx + 1] = arr[lower_idx + 1], arr[end]

    print(" ".join(map(str, arr)))

    quicksort_partial(arr, start, lower_idx)
    quicksort_partial(arr, lower_idx + 2, end)

def quicksort(arr):
    quicksort_partial(arr, 0, len(arr) - 1)

n = int(input())
ar = [int(temp) for temp in input().split(' ')]
assert(len(ar) == n)
quicksort(ar)
