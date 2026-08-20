class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self._items = [None] * capacity
        self._front = 0
        self._rear = -1
        self._size = 0

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("enqueue to full queue")
        self._rear = (self._rear + 1) % self.capacity
        self._items[self._rear] = item
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        item = self._items[self._front]
        self._items[self._front] = None
        self._front = (self._front + 1) % self.capacity
        self._size -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._items[self._front]

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == self.capacity

    def __len__(self):
        return self._size
