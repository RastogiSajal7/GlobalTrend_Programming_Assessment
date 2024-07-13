# Implement a Python class MaxHeap that supports the following operations: insert, delete, and get_max. 
# Ensure the operations maintain the properties of a max-heap.

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, data):
        self.heap.append(data)
        self._heapify_up(len(self.heap) - 1)

    def delete(self, data):
        try:
            index = self.heap.index(data)
            self._swap(index, len(self.heap) - 1)
            removed_value = self.heap.pop()
            if index < len(self.heap):
                self._heapify_down(index)
                self._heapify_up(index)
            return removed_value
        except ValueError:
            return None

    def get_max(self):
        if not self.heap:
            return None
        return self.heap[0]

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self._swap(index, parent_index)
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest = index

        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
            largest = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
            largest = right_child_index

        if largest != index:
            self._swap(index, largest)
            self._heapify_down(largest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __str__(self):
        return str(self.heap)

max_heap = MaxHeap()
max_heap.insert(92)
max_heap.insert(116)
max_heap.insert(5)
max_heap.insert(63)
max_heap.insert(3)

print("The Max-Heap after multiple insertions:", max_heap)
print("The maximum value in the Max-Heap:", max_heap.get_max()) 
print("The value being deleted from the Max-Heap:", max_heap.delete(116)) 
print("The Max-Heap after deleting:", max_heap) 
print("The new maximum value in the Max-Heap after the deletion:", max_heap.get_max())
        