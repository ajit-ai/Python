from collections import deque


def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


def is_same_tree_iterative(p, q):
    queue = deque([(p, q)])
    while queue:
        n1, n2 = queue.popleft()
        if not n1 and not n2:
            continue
        if not n1 or not n2:
            return False
        if n1.val != n2.val:
            return False
        queue.append((n1.left, n2.left))
        queue.append((n1.right, n2.right))
    return True
