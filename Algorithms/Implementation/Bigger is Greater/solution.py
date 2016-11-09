t = int(input())
base_ord = ord('a')

for i in range(t):
    w = input()
    orig_w = w
    w = list(w)
    len_w = len(w)
    char_count = [0] * 26
    char_greater = [False] * 26
    
    if len_w == 1:
        print("no answer")
        continue
    
    # Work backwards from w and find first point where a swap can occur
    val = ord(w[-1]) - base_ord
    char_count[val] += 1
    
    for a in range(val - 1, -1, -1):
        char_greater[a] = True
    
    for j in range(len_w - 2, -1, -1):
        val = ord(w[j]) - base_ord
        char_count[val] += 1
        
        if char_greater[val]:
            # There is a greater value character after this character
            # Find first character greater than current character now
            for a in range(val + 1, 26):
                if char_count[a] > 0:
                    # This character can be used
                    char_count[a] -= 1
                    w[j] = chr(a + base_ord)
                    break
            
            # Fill in rest of the 
            k = 1
            for a in range(26):
                #print(a)
                val2 = chr(a + base_ord)
                
                for b in range(char_count[a]):
                    w[j + k] = val2
                    k += 1
            
            break
        else:
            # Add this character to the pool of characters to swap with
            for a in range(val - 1, -1, -1):
                if char_greater[a]:
                    break

                char_greater[a] = True
        
    w = "".join(w)
    
    if orig_w == w:
        print("no answer")
    else:
        print(w)

