Q = int(input())

s1 = list()
s2 = list()

for q in range(Q):
    query = input().split(' ')
    
    if query[0] == '1':
        s1.append(query[1])
            
    elif query[0] == '2':
        if len(s2) == 0:
            while len(s1) != 0:
                s2.append(s1[-1])
                s1.pop()
        
        s2.pop()
        
    elif query[0] == '3':
        if len(s2) == 0:
            while len(s1) != 0:
                s2.append(s1[-1])
                s1.pop()
        
        print(s2[-1])
    else:
        assert(false)

