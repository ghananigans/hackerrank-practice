n = int(input())
ar = [int(temp) for temp in input().split(' ')]
assert(len(ar) == n)

pivot = ar[0]
left = []
right = []

for a in ar:
    if a < pivot:
        left.append(a)
    elif a > pivot:
        right.append(a)

ar = left + [pivot] + right

print(" ".join(map(str, ar)))
