class ZigZagIterator:
    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.queue = [_ for _ in (v1, v2) if _]
        print(self.queue)

    def next(self):
        """
        :rtype: int
        """
        v = self.queue.pop(0)
        ret = v.pop(0)
        if v:
            self.queue.append(v)
        return ret

    def has_next(self):
        """
        :rtype: bool
        """
        if self.queue:
            return True
        return False

#call class in main method to get result


if __name__ == '__main__':
    
    l1 = [1, 2]
    l2 = [3, 4, 5, 6]
    print(ZigZagIterator(l1, l2))
    print(ZigZagIterator(l1, l2).next())
    print(ZigZagIterator(l1, l2).has_next())
    