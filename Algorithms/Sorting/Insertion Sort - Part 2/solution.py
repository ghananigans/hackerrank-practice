def arr_to_string(arr):
    string = ""

    for a in arr:
        string += str(a) + " "

    return string.strip()

def partialInsertionSort(ar, max_idx):
    if max_idx == 0:
        return ar

    i = max_idx

    while i > 0:
        if ar[i] < ar[i - 1]:
            ar[i], ar[i - 1] = ar[i - 1], ar[i]

        i -= 1

    return ar

def insertionSort(ar):
    s = len(ar)

    for i in range(1, s):
        ar = partialInsertionSort(ar, i)
        print(arr_to_string(ar))



s = int(input())
arr = [int(temp) for temp in input().split(' ')]
assert(len(arr) == s)
insertionSort(arr)
