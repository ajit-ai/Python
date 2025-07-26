"""
Queue Abstract Data Type (ADT)
* Queue() creates a new queue that is empty.
  It needs no parameters and returns an empty queue.
* enqueue(item) adds a new item to the rear of the queue.
  It needs the item and returns nothing.
* dequeue() removes the front item from the queue.
  It needs no parameters and returns the item. The queue is modified.
* isEmpty() tests to see whether the queue is empty.
  It needs no parameters and returns a boolean value.
* size() returns the number of items in the queue.
  It needs no parameters and returns an integer.
* peek() returns the front element of the queue.
"""

from abc import ABCMeta, abstractmethod

class AbstractQueue(metaclass=ABCMeta):
    def __init__(self):
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    @abstractmethod
    def enqueue(self, value):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def peek(self):
        pass

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

class ArrayQueue(AbstractQueue):
    def __init__(self, capacity=10, items=None):
        """
        Initialize an array-based queue with a given capacity or items.
        Uses a circular buffer to optimize space usage.
        """
        super().__init__()
        self._array = [None] * (capacity if items is None else max(capacity, len(items)))
        self._front = 0
        self._rear = 0
        self._capacity = len(self._array)
        if items:
            for item in items:
                self.enqueue(item)

    def __iter__(self):
        probe = self._front
        count = 0
        while count < self._size:
            yield self._array[probe]
            probe = (probe + 1) % self._capacity
            count += 1

    def __str__(self):
        items = [str(item) for item in self]
        return f"ArrayQueue([{', '.join(items)}])"

    def enqueue(self, value):
        if self._size == self._capacity:
            self._expand()
        self._array[self._rear] = value
        self._rear = (self._rear + 1) % self._capacity
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        value = self._array[self._front]
        self._array[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._array[self._front]

    def _expand(self):
        """Expand the array size, maintaining circular buffer properties."""
        new_array = [None] * (self._capacity * 2)
        for i, item in enumerate(self):
            new_array[i] = item
        self._array = new_array
        self._front = 0
        self._rear = self._size
        self._capacity = len(self._array)

class QueueNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListQueue(AbstractQueue):
    def __init__(self, items=None):
        """
        Initialize a linked-list-based queue with optional items.
        """
        super().__init__()
        self._front = None
        self._rear = None
        if items:
            for item in items:
                self.enqueue(item)

    def __iter__(self):
        probe = self._front
        while probe is not None:
            yield probe.value
            probe = probe.next

    def __str__(self):
        items = [str(item) for item in self]
        return f"LinkedListQueue([{', '.join(items)}])"

    def enqueue(self, value):
        node = QueueNode(value)
        if self._front is None:
            self._front = node
            self._rear = node
        else:
            self._rear.next = node
            self._rear = node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        value = self._front.value
        if self._front is self._rear:
            self._front = None
            self._rear = None
        else:
            self._front = self._front.next
        self._size -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._front.value

# Main method to demonstrate queue operations
if __name__ == '__main__':
    # Create empty queues
    array_queue = ArrayQueue()
    linked_queue = LinkedListQueue()
    print("Empty ArrayQueue:", array_queue)
    print("Empty LinkedListQueue:", linked_queue)

    # Create queues with initial items
    array_queue = ArrayQueue(items=[1, 2, 3, 4, 5])
    linked_queue = LinkedListQueue(items=[1, 2, 3, 4, 5])
    print("\nInitial ArrayQueue:", array_queue)
    print("Initial LinkedListQueue:", linked_queue)

    # Test enqueue
    array_queue.enqueue(6)
    linked_queue.enqueue(6)
    print("\nAfter enqueue(6):")
    print("ArrayQueue:", array_queue)
    print("LinkedListQueue:", linked_queue)

    # Test dequeue
    print("\nDequeue results:")
    print("ArrayQueue dequeue:", array_queue.dequeue())
    print("LinkedListQueue dequeue:", linked_queue.dequeue())
    print("ArrayQueue after dequeue:", array_queue)
    print("LinkedListQueue after dequeue:", linked_queue)

    # Test peek
    print("\nPeek results:")
    print("ArrayQueue peek:", array_queue.peek())
    print("LinkedListQueue peek:", linked_queue.peek())

    # Test size and is_empty
    print("\nSize and emptiness check:")
    print("ArrayQueue size:", len(array_queue))
    print("LinkedListQueue size:", len(linked_queue))
    print("ArrayQueue is empty:", array_queue.is_empty())
    print("LinkedListQueue is empty:", linked_queue.is_empty())