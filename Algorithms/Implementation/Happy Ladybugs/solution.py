#!/bin/python3

base_val = ord('A')
Q = int(input().strip())
for a0 in range(Q):
    n = int(input().strip())
    b = input().strip()
    arr = [0] * 26

    spaceless = b.replace("_", "")
    letters = len(spaceless)
    spaces = n - letters

    possible = True

    if spaces == 0:
        if letters == 1:
            possible = False
        elif letters == 2:
            if spaceless[0] != spaceless[1]:
                possible = False
        else:
            if b[0] != b[1]:
                possible = False
            elif b[-2] != b[-1]:
                possible = False
            else:
                for i in range(1, n - 1):
                    if b[i] !=  b[i - 1] and b[i] != b[i + 1]:
                        possible = False
                        break
    else:
        for a in b:
            val = ord(a) - base_val

            if val >= 0 and val < 26: 
                arr[val] += 1

        for a in arr:
            if a == 1:
                possible = False
                break

    print("YES") if possible else print("NO")

