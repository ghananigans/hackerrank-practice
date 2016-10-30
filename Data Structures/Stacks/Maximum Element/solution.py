N = int(input())

data = list()
max_val = 0

for n in range(N):
    query = [temp for temp in input().split(' ')]

    if query[0] == "1":
        max_val = max(int(query[1]), max_val)
        data.append(max_val)
    elif query[0] == "2":
        data.pop()
        
        if len(data) == 0:
            max_val = 0
        else:
            max_val = data[-1]
    elif query[0] == "3":
        print(data[-1])
    else:
        assert( false )

