# 2. (50 pts) For an array-based binary min-heap, please implement the operation DELETE which
# removes an element from the heap, and analyze the running time.

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def delete(self, index):
        # Replaces the elemnt that has to be removed
        last_index = len(self.heap) - 1
        self.heap[index] = self.heap[last_index]
        self.heap.pop()  # Removes the last element

        if index < len(self.heap):
            self._heapify_down(index)

    def _heapify_down(self, i):
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        smallest = i

        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._heapify_down(smallest)

    def _heapify_up(self, i):
        p = (i - 1) // 2
        if i > 0 and self.heap[i] < self.heap[p]:
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            self._heapify_up(p)

    def __str__(self):
        return str(self.heap)


heap = MinHeap()
heap.insert(100)
heap.insert(202)
heap.insert(51)
heap.insert(771)

print("heap before deletion ", heap)

heap.delete(0)
print("heap after deletion ", heap)
