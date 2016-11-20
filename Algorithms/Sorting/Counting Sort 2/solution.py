n = int(input())
arr = [int(temp) for temp in input().split(' ')]

counter = [0] * 100
out_str = ""

for a in arr:
    counter[a] += 1

for i in range(100):
    out_str += (str(i) + " ") * counter[i]

print(out_str.strip())
