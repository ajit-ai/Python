"""
Implementation of priority queue using linear array.
Insertion - O(n)
Extract min/max Node - O(1)
"""
import itertools


class PriorityQueueNode:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority

    def __repr__(self):
        return "{}: {}".format(self.data, self.priority)


class PriorityQueue:
    def __init__(self, items=None, priorities=None):
        """Create a priority queue with items (list or iterable).
        If items is not passed, create empty priority queue."""
        self.priority_queue_list = []
        if items is None:
            return
        if priorities is None:
            priorities = itertools.repeat(None)
        for item, priority in zip(items, priorities):
            self.push(item, priority=priority)

    def __repr__(self):
        return "PriorityQueue({!r})".format(self.priority_queue_list)

    def size(self):
        """Return size of the priority queue.
        """
        return len(self.priority_queue_list)

    def push(self, item, priority=None):
        """Push the item in the priority queue.
        if priority is not given, priority is set to the value of item.
        """
        priority = item if priority is None else priority
        node = PriorityQueueNode(item, priority)
        for index, current in enumerate(self.priority_queue_list):
            if current.priority < node.priority:
                self.priority_queue_list.insert(index, node)
                return
        # when traversed complete queue
        self.priority_queue_list.append(node)

    def pop(self):
        """Remove and return the item with the lowest priority.
        """
        # remove and return the first node from the queue
        return self.priority_queue_list.pop().data


#call main method to get result
if __name__ == '__main__':
    print(PriorityQueue([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]))
    print(PriorityQueue([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]).pop())
    print(PriorityQueue([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]).size())
    print(PriorityQueue([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]).push(6, 6))
    print(PriorityQueue([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]).push(7, 7))