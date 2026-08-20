def validate_bst(root):
    return _validate(root, float('-inf'), float('inf'))


def _validate(node, low, high):
    if node is None:
        return True
    if node.val <= low or node.val >= high:
        return False
    return _validate(node.left, low, node.val) and _validate(node.right, node.val, high)


def validate_bst_inorder(root):
    stack = []
    prev = None
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        if prev is not None and current.val <= prev:
            return False
        prev = current.val
        current = current.right
    return True
