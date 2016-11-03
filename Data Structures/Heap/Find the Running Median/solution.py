class Heap:
    def __init__(self, max_size):
        self.data = [None] * max_size
        self.count = 0

    def reorder_down(self):
        len_heap = self.count

        idx = 0

        while idx < len_heap:
            l = 2 * idx + 1
            r = l + 1

            if l < len_heap and self.data[l] < self.data[idx] and (r >= len_heap or self.data[r] >= self.data[l]):
                self.data[l], self.data[idx] = self.data[idx], self.data[l]
                idx = l
            elif r < len_heap and self.data[r] < self.data[idx] and (l >= len_heap or self.data[l] >= self.data[r]):
                self.data[r], self.data[idx] = self.data[idx], self.data[r]
                idx = r
            else:
                break

    def reorder_up(self):
        len_heap = self.count

        prev_idx = len_heap - 1
        idx = (prev_idx - 1) // 2

        while prev_idx > 0:
            if self.data[idx] <= self.data[prev_idx]:
                break

            self.data[idx], self.data[prev_idx] = self.data[prev_idx], self.data[idx]
            prev_idx = idx
            idx = (prev_idx - 1) // 2

    def pop(self):
        len_heap = self.count

        assert(len_heap > 0)

        if len_heap == 0:
            return None

        ret = self.data[0]
        self.data[0], self.data[len_heap - 1] = self.data[len_heap - 1], self.data[0]
        self.count -= 1

        self.reorder_down()

        return ret

    def insert(self, val):
        self.data[self.count] = val
        self.count += 1
        
        self.reorder_up()
        
    def min(self):
        if self.count == 0:
            return None
        
        return self.data[0]
    
    def size(self):
        return self.count
    
    def arr(self):
        return self.data

N = int(input())

min_heap = Heap((N + 2) // 2)
max_heap = Heap((N + 2) // 2)

even = True

for n in range(N):
    val = int(input())
    
    even = not even
    
    if max_heap.size() == 0:
        max_heap.insert(-1 * val)
    else:
        if val < -1 * max_heap.min():
            max_heap.insert(-1 * val)
        else:
            min_heap.insert(val)
    
        if min_heap.size() > max_heap.size():
            temp = -1 * min_heap.pop()
            max_heap.insert(temp)
        elif max_heap.size() > min_heap.size() + 1:
            temp = -1 * max_heap.pop()
            min_heap.insert(temp)
    
    if even:
        a = -1 * max_heap.min()
        b = min_heap.min()
        
        print("%.1f" % ((a + b) / 2))
    else:
        a = -1 * max_heap.min()
        print("%.1f" % a)

