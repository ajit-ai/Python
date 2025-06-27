import unittest
from sorting import merge_sort


class TestMergeSort(unittest.TestCase):
    def test_sorted_input(self):
        """Test merge_sort with an already sorted list."""
        self.assertEqual(merge_sort([1, 2, 3]), [1, 2, 3])

    def test_reverse_sorted_input(self):
        """Test merge_sort with a reverse-sorted list."""
        self.assertEqual(merge_sort([3, 2, 1]), [1, 2, 3])

    def test_unsorted_input(self):
        """Test merge_sort with an unsorted list (similar to Go test case)."""
        self.assertEqual(merge_sort([97, 122, 109]), [97, 109, 122])

    def test_empty_list(self):
        """Test merge_sort with an empty list."""
        self.assertEqual(merge_sort([]), [])

    def test_single_element(self):
        """Test merge_sort with a single-element list."""
        self.assertEqual(merge_sort([42]), [42])

    def test_duplicate_elements(self):
        """Test merge_sort with duplicate elements."""
        self.assertEqual(merge_sort([5, 2, 5, 1]), [1, 2, 5, 5])


if __name__ == '__main__':
    unittest.main()