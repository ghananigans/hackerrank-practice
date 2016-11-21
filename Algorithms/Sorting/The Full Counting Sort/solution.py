n = int(input())
storage = {}

for i in range(n // 2):
    key, val = input().split(' ')
    key = int(key)
    val = "-"

    if key in storage:
        storage[key].append(val)
    else:
        storage[key] = [val]

for i in range(n // 2):
    key, val = input().split(' ')
    key = int(key)

    if key in storage:
        storage[key].append(val)
    else:
        storage[key] = [val]

out_str = ""

for i in range(100):
    if i in storage:
        out_str += " ".join(storage[i]) + " "

print(out_str.strip())
