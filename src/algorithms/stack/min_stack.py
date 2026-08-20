class MinStack:
    def __init__(self):
        self._stack = []
        self._min_stack = []

    def push(self, val):
        self._stack.append(val)
        if not self._min_stack or val <= self._min_stack[-1]:
            self._min_stack.append(val)

    def pop(self):
        if not self._stack:
            raise IndexError("pop from empty stack")
        val = self._stack.pop()
        if val == self._min_stack[-1]:
            self._min_stack.pop()
        return val

    def top(self):
        if not self._stack:
            raise IndexError("top from empty stack")
        return self._stack[-1]

    def get_min(self):
        if not self._min_stack:
            raise IndexError("get_min from empty stack")
        return self._min_stack[-1]

    def is_empty(self):
        return len(self._stack) == 0

    def __len__(self):
        return len(self._stack)
