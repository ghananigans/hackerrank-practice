#
# Think of each level 0 node as leaf nodes and we are going
# from 1 leaf node (L) to another leaf node (R). So we need to
# go up the tree to the closest common ancestor then go down 
# to the final leaf node.
#
factor_values_storage = dict()
def factor_values(k):
    factor = 0
    parent_factor = 0
    
    if k in factor_values_storage:
        return factor_values_storage[k]
    
    if k == 0:
        factor = 1
        parent_factor = 10
    else:
        if (k - 1) in factor_values_storage:
            factor = factor_values_storage[k - 1][1]
        else:
            factor = 10 ** (2 ** (k - 1))
        
        parent_factor = factor ** 2
        
    factor_values_storage[k] = [factor, parent_factor]
    return [factor, parent_factor]

def position_difference(l, r, parent_factor):
    # Round up l value to nearest parent_factor multiple
    a = ((l + parent_factor) // parent_factor) * parent_factor
    return min(r, a) - l
        
def solution(L, R):
    l = L - 1
    r = R
    k = 0
    result = []
    parent_factor = 0

    # Go up the tree from L to the closest common ancestor to R
    while (r - l) >= parent_factor:
        factor, parent_factor = factor_values(k)
        pos_diff = position_difference(l, r, parent_factor)
        steps = (pos_diff % parent_factor) // factor
        
        while steps == 0:
            k += 1
            factor, parent_factor = factor_values(k)
            pos_diff = position_difference(l, r, parent_factor)
            steps = (pos_diff % parent_factor) // factor
        
        result.append([k, steps])
        l += steps * factor
        k += 1

    # Go down the tree from closest common ancestor between
    # L and R, to R.
    #
    #
    # Use this so we dont have 2 consective entries at
    # the same level (eg. going from 8 to 13 may print
    # 0 3; 0 3 instead of 0 6
    if (r - l) != 0:
        factor, parent_factor = factor_values(k)
        pos_diff = position_difference(l, r, parent_factor)
        steps = (pos_diff % parent_factor) // factor
    
        while steps == 0:
            k -= 1
            factor, parent_factor = factor_values(k)
            pos_diff = position_difference(l, r, parent_factor)
            steps = (pos_diff % parent_factor) // factor

        if result[-1][0] == k:
            result[-1][1] += steps
        else:
            result.append([k, steps])

        l += steps * factor
        k -= 1
    
    # Deal with rest of the path going down the tree to R
    while (r - l) != 0:
        factor, parent_factor = factor_values(k)
        pos_diff = position_difference(l, r, parent_factor)
        steps = (pos_diff % parent_factor) // factor
        
        while steps == 0:
            k -= 1
            factor, parent_factor = factor_values(k)
            pos_diff = position_difference(l, r, parent_factor)
            steps = (pos_diff % parent_factor) // factor
        
        result.append([k, steps])
        l += steps * factor
        k -= 1

    return result

def print_result(result):
    print(len(result))
    
    for r in result:
        print(str(r[0]) + " " + str(r[1]))

L = int(input())
R = int(input())

result = solution(L, R)
print_result(result)

