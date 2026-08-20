def has_path_sum(root, target_sum):
    if root is None:
        return False
    if root.left is None and root.right is None:
        return root.val == target_sum
    remaining = target_sum - root.val
    return has_path_sum(root.left, remaining) or has_path_sum(root.right, remaining)


def path_sum_all(root, target_sum):
    result = []
    _find_paths(root, target_sum, [], result)
    return result


def _find_paths(node, remaining, path, result):
    if node is None:
        return
    path.append(node.val)
    if node.left is None and node.right is None and remaining == node.val:
        result.append(list(path))
    else:
        _find_paths(node.left, remaining - node.val, path, result)
        _find_paths(node.right, remaining - node.val, path, result)
    path.pop()
