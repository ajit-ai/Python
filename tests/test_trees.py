import pytest
from algorithms.trees.bst import (
    TreeNode, insert, search, delete, inorder, from_list
)
from algorithms.trees.traversals import (
    inorder as iter_inorder, preorder, postorder, level_order,
    inorder_recursive, preorder_recursive, postorder_recursive
)
from algorithms.trees.lca import lowest_common_ancestor
from algorithms.trees.validate_bst import validate_bst, validate_bst_inorder
from algorithms.trees.max_depth import max_depth_recursive, max_depth_iterative
from algorithms.trees.balanced import is_balanced
from algorithms.trees.same_tree import is_same_tree, is_same_tree_iterative
from algorithms.trees.subtree import is_subtree
from algorithms.trees.path_sum import has_path_sum, path_sum_all


def _make_bst(values):
    root = None
    for v in values:
        root = insert(root, v)
    return root


def _make_node(val, left=None, right=None):
    return TreeNode(val, left, right)


class TestBST:
    def test_insert_inorder(self):
        root = _make_bst([5, 3, 7, 1, 4, 6, 8])
        assert inorder(root) == [1, 3, 4, 5, 6, 7, 8]

    def test_search_found(self):
        root = _make_bst([5, 3, 7, 1, 4])
        node = search(root, 3)
        assert node is not None and node.val == 3

    def test_search_not_found(self):
        root = _make_bst([5, 3, 7])
        assert search(root, 10) is None

    def test_delete_leaf(self):
        root = _make_bst([5, 3, 7, 1])
        root = delete(root, 1)
        assert inorder(root) == [3, 5, 7]

    def test_delete_one_child(self):
        root = _make_bst([5, 3, 7, 1])
        root = delete(root, 3)
        assert inorder(root) == [1, 5, 7]

    def test_delete_two_children(self):
        root = _make_bst([5, 3, 7, 1, 4, 6, 8])
        root = delete(root, 5)
        assert inorder(root) == [1, 3, 4, 6, 7, 8]

    def test_empty_tree(self):
        assert inorder(None) == []

    def test_single_node(self):
        root = from_list([42])
        assert inorder(root) == [42]


class TestTraversals:
    @pytest.fixture
    def tree(self):
        root = _make_node(1,
            _make_node(2, _make_node(4), _make_node(5)),
            _make_node(3, _make_node(6), _make_node(7))
        )
        return root

    def test_inorder_iter(self, tree):
        assert iter_inorder(tree) == [4, 2, 5, 1, 6, 3, 7]

    def test_preorder_iter(self, tree):
        assert preorder(tree) == [1, 2, 4, 5, 3, 6, 7]

    def test_postorder_iter(self, tree):
        assert postorder(tree) == [4, 5, 2, 6, 7, 3, 1]

    def test_level_order(self, tree):
        assert level_order(tree) == [[1], [2, 3], [4, 5, 6, 7]]

    def test_inorder_recursive(self, tree):
        assert inorder_recursive(tree) == [4, 2, 5, 1, 6, 3, 7]

    def test_preorder_recursive(self, tree):
        assert preorder_recursive(tree) == [1, 2, 4, 5, 3, 6, 7]

    def test_postorder_recursive(self, tree):
        assert postorder_recursive(tree) == [4, 5, 2, 6, 7, 3, 1]

    def test_empty(self):
        assert iter_inorder(None) == []
        assert preorder(None) == []
        assert postorder(None) == []
        assert level_order(None) == []


class TestLCA:
    def test_common_ancestor(self):
        root = _make_bst([6, 2, 8, 0, 4, 7, 9, 3, 5])
        p = search(root, 2)
        q = search(root, 8)
        assert lowest_common_ancestor(root, p, q).val == 6

    def test_same_subtree(self):
        root = _make_bst([6, 2, 8, 0, 4, 7, 9])
        p = search(root, 2)
        q = search(root, 4)
        assert lowest_common_ancestor(root, p, q).val == 2

    def test_root_is_lca(self):
        root = _make_bst([3, 1, 5])
        p = search(root, 1)
        q = search(root, 5)
        assert lowest_common_ancestor(root, p, q).val == 3

    def test_one_node_is_ancestor(self):
        root = _make_node(1, _make_node(2))
        assert lowest_common_ancestor(root, root, root.left).val == 1


class TestValidateBST:
    def test_valid(self):
        root = _make_bst([5, 3, 7, 1, 4])
        assert validate_bst(root) is True

    def test_invalid(self):
        root = _make_node(5, _make_node(1), _make_node(7, _make_node(6), _make_node(8)))
        left_wrong = _make_node(5, _make_node(1, right=_make_node(6)), _make_node(7))
        assert validate_bst(left_wrong) is False

    def test_empty(self):
        assert validate_bst(None) is True

    def test_inorder_valid(self):
        root = _make_bst([10, 5, 15, 2, 7])
        assert validate_bst_inorder(root) is True

    def test_inorder_invalid(self):
        root = _make_node(5, _make_node(1), _make_node(7, _make_node(4), _make_node(8)))
        assert validate_bst_inorder(root) is False

    def test_duplicate_values(self):
        root = _make_node(2, _make_node(2), _make_node(3))
        assert validate_bst(root) is False


class TestMaxDepth:
    def test_basic(self):
        root = _make_node(3,
            _make_node(9),
            _make_node(20, _make_node(15), _make_node(7))
        )
        assert max_depth_recursive(root) == 3
        assert max_depth_iterative(root) == 3

    def test_empty(self):
        assert max_depth_recursive(None) == 0
        assert max_depth_iterative(None) == 0

    def test_single(self):
        root = _make_node(1)
        assert max_depth_recursive(root) == 1
        assert max_depth_iterative(root) == 1

    def test_left_skewed(self):
        root = _make_node(1, _make_node(2, _make_node(3)))
        assert max_depth_recursive(root) == 3

    def test_right_skewed(self):
        root = _make_node(1, right=_make_node(2, right=_make_node(3)))
        assert max_depth_iterative(root) == 3


class TestBalanced:
    def test_balanced(self):
        root = _make_node(3,
            _make_node(9),
            _make_node(20, _make_node(15), _make_node(7))
        )
        assert is_balanced(root) is True

    def test_unbalanced(self):
        root = _make_node(1,
            _make_node(2, _make_node(3, _make_node(4)))
        )
        assert is_balanced(root) is False

    def test_empty(self):
        assert is_balanced(None) is True

    def test_single(self):
        assert is_balanced(_make_node(1)) is True

    def test_complete_tree(self):
        root = _make_node(1,
            _make_node(2, _make_node(4), _make_node(5)),
            _make_node(3, _make_node(6), _make_node(7))
        )
        assert is_balanced(root) is True


class TestSameTree:
    def test_same(self):
        a = _make_node(1, _make_node(2), _make_node(3))
        b = _make_node(1, _make_node(2), _make_node(3))
        assert is_same_tree(a, b) is True
        assert is_same_tree_iterative(a, b) is True

    def test_different(self):
        a = _make_node(1, _make_node(2))
        b = _make_node(1, right=_make_node(2))
        assert is_same_tree(a, b) is False

    def test_both_empty(self):
        assert is_same_tree(None, None) is True

    def test_one_empty(self):
        a = _make_node(1)
        assert is_same_tree(a, None) is False

    def test_different_values(self):
        a = _make_node(1, _make_node(2))
        b = _make_node(1, _make_node(3))
        assert is_same_tree(a, b) is False


class TestSubtree:
    def test_is_subtree(self):
        tree = _make_node(3,
            _make_node(4, _make_node(1), _make_node(2)),
            _make_node(5)
        )
        sub = _make_node(4, _make_node(1), _make_node(2))
        assert is_subtree(tree, sub) is True

    def test_not_subtree(self):
        tree = _make_node(3,
            _make_node(4, _make_node(1), _make_node(2)),
            _make_node(5)
        )
        sub = _make_node(4, _make_node(1), _make_node(3))
        assert is_subtree(tree, sub) is False

    def test_empty_subtree(self):
        assert is_subtree(_make_node(1), None) is True

    def test_same_tree(self):
        a = _make_node(1, _make_node(2))
        assert is_subtree(a, a) is True


class TestPathSum:
    def test_has_path(self):
        root = _make_node(5,
            _make_node(4, _make_node(11, _make_node(7), _make_node(2))),
            _make_node(8, _make_node(13), _make_node(4, right=_make_node(1)))
        )
        assert has_path_sum(root, 22) is True

    def test_no_path(self):
        root = _make_node(1, _make_node(2), _make_node(3))
        assert has_path_sum(root, 5) is False

    def test_empty(self):
        assert has_path_sum(None, 0) is False

    def test_single_match(self):
        assert has_path_sum(_make_node(1), 1) is True

    def test_single_no_match(self):
        assert has_path_sum(_make_node(1), 0) is False

    def test_path_sum_all(self):
        root = _make_node(5,
            _make_node(4, _make_node(11, _make_node(7), _make_node(2))),
            _make_node(8, _make_node(13), _make_node(4, _make_node(5), _make_node(1)))
        )
        result = path_sum_all(root, 22)
        assert [5, 4, 11, 2] in result
