import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'algorithms', 'linkedlist'))

from is_cyclic import Node as CyclicNode, is_cyclic
from merge_two_list import Node as ListNode, merge_two_list
from reverse import reverse_list


def build_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


class TestIsCyclic:
    def test_no_cycle(self):
        head = CyclicNode(1)
        head.next = CyclicNode(2)
        head.next.next = CyclicNode(3)
        assert is_cyclic(head) is False

    def test_cycle(self):
        head = CyclicNode(1)
        node2 = CyclicNode(2)
        node3 = CyclicNode(3)
        head.next = node2
        node2.next = node3
        node3.next = node2
        assert is_cyclic(head) is True

    def test_empty(self):
        assert is_cyclic(None) is False

    def test_single_no_cycle(self):
        head = CyclicNode(1)
        assert is_cyclic(head) is False


class TestMergeTwoList:
    def test_basic(self):
        l1 = build_list([1, 2, 4])
        l2 = build_list([1, 3, 4])
        result = merge_two_list(l1, l2)
        assert list_to_array(result) == [1, 1, 2, 3, 4, 4]

    def test_one_empty(self):
        l1 = build_list([1, 2, 3])
        result = merge_two_list(l1, None)
        assert list_to_array(result) == [1, 2, 3]

    def test_both_empty(self):
        result = merge_two_list(None, None)
        assert result is None


class TestReverseList:
    def test_basic(self):
        head = build_list([1, 2, 3, 4, 5])
        result = reverse_list(head)
        assert list_to_array(result) == [5, 4, 3, 2, 1]

    def test_single(self):
        head = build_list([1])
        result = reverse_list(head)
        assert list_to_array(result) == [1]

    def test_empty(self):
        assert reverse_list(None) is None
