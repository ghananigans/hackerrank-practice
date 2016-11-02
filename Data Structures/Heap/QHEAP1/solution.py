def reorder_up(heap):
    prev_idx = len(heap) - 1
        
    idx = (prev_idx - 1) // 2

    while prev_idx > 0 and prev_idx != idx:
        if heap[idx] <= heap[prev_idx]:
            break
            
        heap[idx], heap[prev_idx] = heap[prev_idx], heap[idx]

        prev_idx = idx
        idx = (prev_idx - 1) // 2

def reorder_down(heap, start_idx):
    idx = start_idx
    len_heap = len(heap)
    
    while idx < len_heap:
        l = 2 * idx + 1
        r = l + 1
        
        if l < len_heap and heap[l] < heap[idx] and (r >= len_heap or heap[l] < heap[r]):
            heap[l], heap[idx] = heap[idx], heap[l]
            idx = l
        elif r < len_heap and heap[r] < heap[idx] and (l >= len_heap or heap[r] < heap[l]) :
            heap[r], heap[idx] = heap[idx], heap[r]
            idx = r
        else:
            break
            
def insert(heap, val):
    heap.append(val)
    reorder_up(heap)

def delete(heap, val):
    len_heap = len(heap)
    
    assert(len_heap != 0)
    
    idx = heap.index(val)
    assert(heap[idx] == val)

    if idx != len_heap - 1:
        heap[-1], heap[idx] = heap[idx], heap[-1]
    
    heap.pop()
    
    reorder_down(heap, idx)

Q = int(input())
heap = list()

for q in range(Q):
    command = input().split(' ')
    
    if command[0] == '1':
        insert(heap, int(command[1]))
    elif command[0] == '2':
        delete(heap, int(command[1]))
    elif command[0] == '3':
        if len(heap) == 0:
            assert(false)
                
        print(heap[0])
    else:
        assert(false)

