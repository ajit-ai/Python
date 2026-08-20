def is_balanced(root):
    return _check_height(root) != -1


def _check_height(node):
    if node is None:
        return 0
    left = _check_height(node.left)
    if left == -1:
        return -1
    right = _check_height(node.right)
    if right == -1:
        return -1
    if abs(left - right) > 1:
        return -1
    return 1 + max(left, right)
