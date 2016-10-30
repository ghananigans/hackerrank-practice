Q = int(input())

S = ""
queries = list()

for q in range(Q):
    temp = input().split(' ')
    
    if temp[0] == '1':
        # Append
        S += temp[1]
        queries.append(['1', len(temp[1])])
    elif temp[0] == '2':
        # Delete
        k = -1 * int(temp[1])
        queries.append(['2', S[k:]])
        S = S[:k]
    elif temp[0] == '3':
        # Print
        k = int(temp[1]) - 1
        print(S[k])
    elif temp[0] == '4':
        # Undo
        
        # queries length should never be 0 if we
        # are undoing
        assert(len(queries) != 0)
        
        if queries[-1][0] == '1':
            # Append before so remove now
            k = -1 * queries[-1][1]
            S = S[:k]
        elif queries[-1][0] == '2':
            # Delete before so append now
            S += queries[-1][1]
        else:
            # Should never end up here
            assert(false)
        
        queries.pop()
        
    else:
        # Should never end up here
        assert(false)

