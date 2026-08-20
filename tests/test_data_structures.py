import pytest

from algorithms.queue.queue import Queue
from algorithms.queue.circular_queue import CircularQueue
from algorithms.heap.priority_queue import PriorityQueue, MinHeap
from algorithms.heap.kth_largest import kth_largest, kth_largest_sort
from algorithms.trie.trie import Trie
from algorithms.union_find.union_find import UnionFind
from algorithms.stack.min_stack import MinStack
from algorithms.stack.next_greater_element import next_greater_element, next_greater_element_circular
from algorithms.linkedlist.linkedlist_utils import (
    Node, detect_cycle_start, merge_two_sorted_lists,
    remove_nth_from_end, list_to_array, array_to_list,
)
from algorithms.linkedlist.lru_cache import LRUCache


class TestQueue:
    def test_enqueue_and_dequeue(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        assert q.dequeue() == 1
        assert q.dequeue() == 2

    def test_peek(self):
        q = Queue()
        q.enqueue(10)
        q.enqueue(20)
        assert q.peek() == 10
        assert q.peek() == 10

    def test_is_empty(self):
        q = Queue()
        assert q.is_empty() is True
        q.enqueue(1)
        assert q.is_empty() is False

    def test_len(self):
        q = Queue()
        assert len(q) == 0
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        assert len(q) == 3
        q.dequeue()
        assert len(q) == 2

    def test_dequeue_empty_raises(self):
        q = Queue()
        with pytest.raises(IndexError):
            q.dequeue()

    def test_peek_empty_raises(self):
        q = Queue()
        with pytest.raises(IndexError):
            q.peek()

    def test_fifo_order(self):
        q = Queue()
        for i in range(10):
            q.enqueue(i)
        for i in range(10):
            assert q.dequeue() == i


class TestCircularQueue:
    def test_enqueue_dequeue(self):
        cq = CircularQueue(3)
        cq.enqueue(1)
        cq.enqueue(2)
        cq.enqueue(3)
        assert cq.dequeue() == 1
        assert cq.dequeue() == 2
        assert cq.dequeue() == 3

    def test_is_full(self):
        cq = CircularQueue(2)
        assert cq.is_full() is False
        cq.enqueue(1)
        cq.enqueue(2)
        assert cq.is_full() is True

    def test_enqueue_full_raises(self):
        cq = CircularQueue(1)
        cq.enqueue(10)
        with pytest.raises(OverflowError):
            cq.enqueue(20)

    def test_peek(self):
        cq = CircularQueue(3)
        cq.enqueue(5)
        assert cq.peek() == 5
        cq.enqueue(6)
        assert cq.peek() == 5

    def test_wrap_around(self):
        cq = CircularQueue(3)
        cq.enqueue(1)
        cq.enqueue(2)
        cq.enqueue(3)
        cq.dequeue()
        cq.enqueue(4)
        assert cq.dequeue() == 2
        assert cq.dequeue() == 3
        assert cq.dequeue() == 4

    def test_len(self):
        cq = CircularQueue(3)
        assert len(cq) == 0
        cq.enqueue(1)
        cq.enqueue(2)
        assert len(cq) == 2
        cq.dequeue()
        assert len(cq) == 1

    def test_dequeue_empty_raises(self):
        cq = CircularQueue(2)
        with pytest.raises(IndexError):
            cq.dequeue()

    def test_is_empty(self):
        cq = CircularQueue(1)
        assert cq.is_empty() is True
        cq.enqueue(1)
        assert cq.is_empty() is False


class TestPriorityQueue:
    def test_push_and_pop(self):
        pq = PriorityQueue()
        pq.push("low", 10)
        pq.push("high", 1)
        pq.push("mid", 5)
        assert pq.pop() == "high"
        assert pq.pop() == "mid"
        assert pq.pop() == "low"

    def test_peek(self):
        pq = PriorityQueue()
        pq.push("a", 3)
        pq.push("b", 1)
        assert pq.peek() == "b"
        assert pq.peek() == "b"

    def test_is_empty(self):
        pq = PriorityQueue()
        assert pq.is_empty() is True
        pq.push("x", 1)
        assert pq.is_empty() is False

    def test_len(self):
        pq = PriorityQueue()
        assert len(pq) == 0
        pq.push("a", 1)
        pq.push("b", 2)
        assert len(pq) == 2
        pq.pop()
        assert len(pq) == 1

    def test_pop_empty_raises(self):
        pq = PriorityQueue()
        with pytest.raises(IndexError):
            pq.pop()

    def test_same_priority_fifo(self):
        pq = PriorityQueue()
        pq.push("first", 1)
        pq.push("second", 1)
        assert pq.pop() == "first"
        assert pq.pop() == "second"


class TestMinHeap:
    def test_push_and_pop(self):
        h = MinHeap()
        h.push(5)
        h.push(3)
        h.push(8)
        h.push(1)
        assert h.pop() == 1
        assert h.pop() == 3
        assert h.pop() == 5
        assert h.pop() == 8

    def test_peek(self):
        h = MinHeap()
        h.push(10)
        h.push(2)
        assert h.peek() == 2

    def test_size(self):
        h = MinHeap()
        assert h.size() == 0
        h.push(1)
        h.push(2)
        assert h.size() == 2
        h.pop()
        assert h.size() == 1

    def test_pop_empty_raises(self):
        h = MinHeap()
        with pytest.raises(IndexError):
            h.pop()

    def test_single_element(self):
        h = MinHeap()
        h.push(42)
        assert h.peek() == 42
        assert h.pop() == 42
        assert h.size() == 0

    def test_heap_property_maintained(self):
        h = MinHeap()
        vals = [9, 4, 7, 1, 3, 6, 8, 2, 5]
        for v in vals:
            h.push(v)
        result = [h.pop() for _ in range(len(vals))]
        assert result == sorted(vals)


class TestKthLargest:
    def test_basic(self):
        assert kth_largest([3, 2, 1, 5, 6, 4], 2) == 5

    def test_sort_basic(self):
        assert kth_largest_sort([3, 2, 1, 5, 6, 4], 2) == 5

    def test_single_element(self):
        assert kth_largest([1], 1) == 1
        assert kth_largest_sort([1], 1) == 1

    def test_duplicates(self):
        assert kth_largest([3, 3, 3, 3], 1) == 3
        assert kth_largest_sort([3, 3, 3, 3], 1) == 3

    def test_k_equals_length(self):
        assert kth_largest([5, 3, 1, 4, 2], 5) == 1
        assert kth_largest_sort([5, 3, 1, 4, 2], 5) == 1

    def test_negative_numbers(self):
        assert kth_largest([-1, -2, -3, -4], 2) == -2
        assert kth_largest_sort([-1, -2, -3, -4], 2) == -2

    def test_both_algorithms_agree(self):
        nums = [7, 10, 4, 3, 20, 15]
        for k in range(1, len(nums) + 1):
            assert kth_largest(nums, k) == kth_largest_sort(nums, k)


class TestTrie:
    def test_insert_and_search(self):
        t = Trie()
        t.insert("hello")
        assert t.search("hello") is True
        assert t.search("hell") is False

    def test_starts_with(self):
        t = Trie()
        t.insert("hello")
        assert t.starts_with("hel") is True
        assert t.starts_with("xyz") is False

    def test_empty_string(self):
        t = Trie()
        assert t.search("") is False
        assert t.starts_with("") is True

    def test_multiple_words(self):
        t = Trie()
        t.insert("apple")
        t.insert("app")
        t.insert("application")
        assert t.search("app") is True
        assert t.search("ap") is False
        assert t.starts_with("ap") is True

    def test_delete(self):
        t = Trie()
        t.insert("hello")
        t.insert("help")
        t.delete("hello")
        assert t.search("hello") is False
        assert t.search("help") is True

    def test_get_all_words(self):
        t = Trie()
        t.insert("cat")
        t.insert("car")
        t.insert("cap")
        words = t.get_all_words()
        assert sorted(words) == sorted(["cat", "car", "cap"])

    def test_delete_nonexistent(self):
        t = Trie()
        t.insert("hello")
        t.delete("world")
        assert t.search("hello") is True

    def test_overlapping_prefixes(self):
        t = Trie()
        t.insert("a")
        t.insert("ab")
        t.insert("abc")
        assert t.search("a") is True
        assert t.search("ab") is True
        assert t.search("abc") is True
        assert t.starts_with("ab") is True


class TestUnionFind:
    def test_basic_union(self):
        uf = UnionFind(5)
        uf.union(0, 1)
        uf.union(2, 3)
        assert uf.connected(0, 1) is True
        assert uf.connected(0, 2) is False

    def test_transitive_union(self):
        uf = UnionFind(5)
        uf.union(0, 1)
        uf.union(1, 2)
        assert uf.connected(0, 2) is True

    def test_components(self):
        uf = UnionFind(5)
        assert uf.components() == 5
        uf.union(0, 1)
        assert uf.components() == 4
        uf.union(2, 3)
        assert uf.components() == 3

    def test_no_op_union(self):
        uf = UnionFind(3)
        uf.union(0, 1)
        uf.union(0, 1)
        assert uf.components() == 2

    def test_union_all(self):
        uf = UnionFind(4)
        for i in range(1, 4):
            uf.union(0, i)
        assert uf.connected(0, 3) is True
        assert uf.components() == 1

    def test_single_element(self):
        uf = UnionFind(1)
        assert uf.components() == 1
        assert uf.find(0) == uf.find(0)

    def test_find_returns_root(self):
        uf = UnionFind(5)
        uf.union(0, 1)
        uf.union(2, 0)
        root = uf.find(1)
        assert uf.find(0) == root
        assert uf.find(2) == root


class TestMinStack:
    def test_push_and_top(self):
        s = MinStack()
        s.push(3)
        s.push(1)
        s.push(5)
        assert s.top() == 5
        assert s.get_min() == 1

    def test_pop(self):
        s = MinStack()
        s.push(2)
        s.push(1)
        assert s.pop() == 1
        assert s.get_min() == 2
        assert s.pop() == 2

    def test_get_min_complex(self):
        s = MinStack()
        s.push(5)
        s.push(3)
        s.push(7)
        s.push(1)
        assert s.get_min() == 1
        s.pop()
        assert s.get_min() == 3
        s.pop()
        assert s.get_min() == 3

    def test_is_empty(self):
        s = MinStack()
        assert s.is_empty() is True
        s.push(1)
        assert s.is_empty() is False

    def test_len(self):
        s = MinStack()
        assert len(s) == 0
        s.push(1)
        s.push(2)
        assert len(s) == 2
        s.pop()
        assert len(s) == 1

    def test_pop_empty_raises(self):
        s = MinStack()
        with pytest.raises(IndexError):
            s.pop()

    def test_top_empty_raises(self):
        s = MinStack()
        with pytest.raises(IndexError):
            s.top()

    def test_single_element_min(self):
        s = MinStack()
        s.push(42)
        assert s.get_min() == 42
        assert s.top() == 42
        s.pop()
        assert s.is_empty() is True


class TestNextGreaterElement:
    def test_basic(self):
        assert next_greater_element([4, 5, 2, 25]) == [5, 25, 25, -1]

    def test_circular(self):
        assert next_greater_element_circular([1, 2, 1]) == [2, -1, 2]

    def test_descending(self):
        assert next_greater_element([5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1]

    def test_single_element(self):
        assert next_greater_element([1]) == [-1]
        assert next_greater_element_circular([1]) == [-1]

    def test_empty(self):
        assert next_greater_element([]) == []
        assert next_greater_element_circular([]) == []

    def test_duplicates(self):
        assert next_greater_element([1, 1, 1]) == [-1, -1, -1]

    def test_circular_wraps(self):
        assert next_greater_element_circular([3, 1, 2]) == [-1, 2, 3]


class TestLinkedListUtils:
    def test_array_to_list_and_back(self):
        arr = [1, 2, 3, 4]
        head = array_to_list(arr)
        assert list_to_array(head) == arr

    def test_empty_list(self):
        assert list_to_array(None) == []
        assert array_to_list([]) is None

    def test_single_element(self):
        head = array_to_list([1])
        assert list_to_array(head) == [1]

    def test_merge_two_sorted(self):
        l1 = array_to_list([1, 3, 5])
        l2 = array_to_list([2, 4, 6])
        merged = merge_two_sorted_lists(l1, l2)
        assert list_to_array(merged) == [1, 2, 3, 4, 5, 6]

    def test_merge_one_empty(self):
        l1 = array_to_list([1, 2])
        merged = merge_two_sorted_lists(l1, None)
        assert list_to_array(merged) == [1, 2]

    def test_merge_both_empty(self):
        assert merge_two_sorted_lists(None, None) is None

    def test_remove_nth_from_end(self):
        head = array_to_list([1, 2, 3, 4, 5])
        result = remove_nth_from_end(head, 2)
        assert list_to_array(result) == [1, 2, 3, 5]

    def test_remove_first(self):
        head = array_to_list([1, 2])
        result = remove_nth_from_end(head, 2)
        assert list_to_array(result) == [2]


class TestLRUCache:
    def test_basic_put_get(self):
        cache = LRUCache(2)
        cache.put(1, "a")
        assert cache.get(1) == "a"

    def test_eviction(self):
        cache = LRUCache(2)
        cache.put(1, "a")
        cache.put(2, "b")
        cache.put(3, "c")
        assert cache.get(1) == -1

    def test_get_refreshes(self):
        cache = LRUCache(2)
        cache.put(1, "a")
        cache.put(2, "b")
        cache.get(1)
        cache.put(3, "c")
        assert cache.get(1) == "a"

    def test_len(self):
        cache = LRUCache(2)
        assert len(cache) == 0
        cache.put(1, "a")
        assert len(cache) == 1
        cache.put(2, "b")
        assert len(cache) == 2

    def test_contains(self):
        cache = LRUCache(2)
        cache.put(1, "a")
        assert 1 in cache
        assert 2 not in cache

    def test_overwrite(self):
        cache = LRUCache(2)
        cache.put(1, "a")
        cache.put(1, "b")
        assert cache.get(1) == "b"
        assert len(cache) == 1

    def test_get_missing(self):
        cache = LRUCache(1)
        assert cache.get(999) == -1

    def test_capacity_one(self):
        cache = LRUCache(1)
        cache.put(1, "a")
        cache.put(2, "b")
        assert cache.get(1) == -1
        assert cache.get(2) == "b"
