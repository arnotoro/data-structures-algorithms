class MinHeap:
    def __init__(self, A: list):
        self.heap = A
        for i in range(len(A)//2, -1, -1):
            self.heapify(i)

    def heapify(self, index: int):
        left_child_index = 2*index + 1
        right_child_index = 2*index + 2
        smallest = index

        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
            smallest = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
            smallest = right_child_index

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify(smallest)
        
    def push(self, key: int):
        self.heap.append(key)
        index = len(self.heap) - 1
        while index > 0:
            parent_index = (index -1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break
        
    def pop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        key = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify(0)
        return key
    
    def print(self):
        for i in self.heap:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    heap = MinHeap([4, 8, 6, 5, 1, 2, 3])
    heap.print()        # 1 4 2 5 8 6 3 
    print(heap.pop())   # 1
    heap.push(9)
    heap.print()        # 2 4 3 5 8 6 9