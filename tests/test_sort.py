from algorithms.sort.bubble_sort import bubble_sort
from algorithms.sort.merge_sort import merge_sort
from algorithms.sort.quick_sort import quick_sort
from algorithms.sort.insertion_sort import insertion_sort
from algorithms.sort.selection_sort import selection_sort
from algorithms.sort.counting_sort import counting_sort
from algorithms.sort.shell_sort import shell_sort


class TestBubbleSort:
    def test_basic(self):
        assert bubble_sort([5, 3, 1, 4, 2]) == [1, 2, 3, 4, 5]

    def test_sorted(self):
        assert bubble_sort([1, 2, 3]) == [1, 2, 3]

    def test_reverse(self):
        assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_duplicates(self):
        assert bubble_sort([3, 1, 3, 1]) == [1, 1, 3, 3]

    def test_single(self):
        assert bubble_sort([1]) == [1]

    def test_empty(self):
        assert bubble_sort([]) == []


class TestMergeSort:
    def test_basic(self):
        assert merge_sort([5, 3, 1, 4, 2]) == [1, 2, 3, 4, 5]

    def test_sorted(self):
        assert merge_sort([1, 2, 3]) == [1, 2, 3]

    def test_single(self):
        assert merge_sort([1]) == [1]

    def test_empty(self):
        assert merge_sort([]) == []

    def test_strings(self):
        assert merge_sort(["banana", "apple", "cherry"]) == ["apple", "banana", "cherry"]


class TestQuickSort:
    def test_basic(self):
        assert quick_sort([5, 3, 1, 4, 2]) == [1, 2, 3, 4, 5]

    def test_sorted(self):
        assert quick_sort([1, 2, 3]) == [1, 2, 3]

    def test_single(self):
        assert quick_sort([1]) == [1]

    def test_empty(self):
        assert quick_sort([]) == []


class TestInsertionSort:
    def test_basic(self):
        assert insertion_sort([5, 3, 1, 4, 2]) == [1, 2, 3, 4, 5]

    def test_sorted(self):
        assert insertion_sort([1, 2, 3]) == [1, 2, 3]

    def test_single(self):
        assert insertion_sort([1]) == [1]

    def test_empty(self):
        assert insertion_sort([]) == []


class TestSelectionSort:
    def test_basic(self):
        assert selection_sort([5, 3, 1, 4, 2]) == [1, 2, 3, 4, 5]

    def test_sorted(self):
        assert selection_sort([1, 2, 3]) == [1, 2, 3]

    def test_single(self):
        assert selection_sort([1]) == [1]

    def test_empty(self):
        assert selection_sort([]) == []


class TestCountingSort:
    def test_basic(self):
        assert counting_sort([4, 2, 2, 8, 3, 3, 1]) == [1, 2, 2, 3, 3, 4, 8]

    def test_sorted(self):
        assert counting_sort([1, 2, 3]) == [1, 2, 3]

    def test_duplicates(self):
        assert counting_sort([5, 5, 5]) == [5, 5, 5]


class TestShellSort:
    def test_basic(self):
        assert shell_sort([5, 3, 1, 4, 2]) == [1, 2, 3, 4, 5]

    def test_sorted(self):
        assert shell_sort([1, 2, 3]) == [1, 2, 3]

    def test_single(self):
        assert shell_sort([1]) == [1]

    def test_empty(self):
        assert shell_sort([]) == []
