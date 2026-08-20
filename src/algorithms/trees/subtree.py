def is_subtree(root, sub_root):
    if sub_root is None:
        return True
    if root is None:
        return False
    if _is_same(root, sub_root):
        return True
    return is_subtree(root.left, sub_root) or is_subtree(root.right, sub_root)


def _is_same(s, t):
    if not s and not t:
        return True
    if not s or not t:
        return False
    if s.val != t.val:
        return False
    return _is_same(s.left, t.left) and _is_same(s.right, t.right)
