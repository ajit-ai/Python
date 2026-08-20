class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def detect_cycle_start(head):
    if not head or not head.next:
        return None
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None


def merge_two_sorted_lists(l1, l2):
    dummy = Node()
    current = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 or l2
    return dummy.next


def remove_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head
    fast = slow = dummy
    for _ in range(n + 1):
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next


def list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def array_to_list(arr):
    dummy = Node()
    current = dummy
    for val in arr:
        current.next = Node(val)
        current = current.next
    return dummy.next
