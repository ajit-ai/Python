import heapq


class PriorityQueue:
    def __init__(self):
        self._heap = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._heap, (priority, self._index, item))
        self._index += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty priority queue")
        priority, _, item = heapq.heappop(self._heap)
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty priority queue")
        return self._heap[0][2]

    def is_empty(self):
        return len(self._heap) == 0

    def __len__(self):
        return len(self._heap)


class MinHeap:
    def __init__(self):
        self._heap = []

    def push(self, val):
        self._heap.append(val)
        self._sift_up(len(self._heap) - 1)

    def pop(self):
        if not self._heap:
            raise IndexError("pop from empty heap")
        self._swap(0, len(self._heap) - 1)
        val = self._heap.pop()
        if self._heap:
            self._sift_down(0)
        return val

    def peek(self):
        if not self._heap:
            raise IndexError("peek from empty heap")
        return self._heap[0]

    def size(self):
        return len(self._heap)

    def _sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self._heap[i] < self._heap[parent]:
                self._swap(i, parent)
                i = parent
            else:
                break

    def _sift_down(self, i):
        n = len(self._heap)
        while True:
            smallest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and self._heap[left] < self._heap[smallest]:
                smallest = left
            if right < n and self._heap[right] < self._heap[smallest]:
                smallest = right
            if smallest == i:
                break
            self._swap(i, smallest)
            i = smallest

    def _swap(self, i, j):
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]
