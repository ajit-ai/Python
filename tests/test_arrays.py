import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'algorithms', 'arrays'))

from two_sum import two_sum
from flatten import flatten, flatten_iter
from remove_duplicates import remove_duplicates
from rotate import rotate_v1, rotate_v2, rotate_v3
from move_zeros import move_zeros
from plus_one import plus_one_v1, plus_one_v2, plus_one_v3
from max_ones_index import max_ones_index
from limit import limit
from three_sum import three_sum
from summarize_ranges import summarize_ranges
from missing_ranges import missing_ranges
from trimmean import trimmean
from top_1 import top_1
from delete_nth import delete_nth, delete_nth_naive


class TestTwoSum:
    def test_basic(self):
        assert two_sum([2, 7, 11, 15], 9) == (0, 1)

    def test_middle_elements(self):
        assert two_sum([3, 2, 4], 6) == (1, 2)

    def test_same_element(self):
        assert two_sum([3, 3], 6) == (0, 1)

    def test_no_solution(self):
        assert two_sum([1, 2, 3], 7) is None

    def test_negative_numbers(self):
        assert two_sum([-1, -2, -3, -4, -5], -8) == (2, 4)


class TestFlatten:
    def test_deep_nested(self):
        assert flatten([1, [2, [3, [4]], 5]]) == [1, 2, 3, 4, 5]

    def test_already_flat(self):
        assert flatten([1, 2, 3]) == [1, 2, 3]

    def test_empty(self):
        assert flatten([]) == []

    def test_strings_not_flattened(self):
        assert flatten(["abc", ["def"]]) == ["abc", "def"]

    def test_mixed(self):
        assert flatten([1, [2, 3], [4, [5, [6]]]]) == [1, 2, 3, 4, 5, 6]

    def test_flatten_iter(self):
        assert list(flatten_iter([1, [2, [3, 4]], 5])) == [1, 2, 3, 4, 5]


class TestRemoveDuplicates:
    def test_basic(self):
        assert remove_duplicates([1, 2, 3, 1, 2]) == [1, 2, 3]

    def test_all_same(self):
        assert remove_duplicates([1, 1, 1]) == [1]

    def test_no_duplicates(self):
        assert remove_duplicates([1, 2, 3]) == [1, 2, 3]

    def test_empty(self):
        assert remove_duplicates([]) == []

    def test_strings(self):
        assert remove_duplicates(["a", "b", "a"]) == ["a", "b"]


class TestRotate:
    def test_v1(self):
        assert rotate_v1([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

    def test_v2(self):
        assert rotate_v2([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

    def test_v3(self):
        assert rotate_v3([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

    def test_rotate_by_length(self):
        assert rotate_v1([1, 2, 3], 3) == [1, 2, 3]

    def test_rotate_zero(self):
        assert rotate_v1([1, 2, 3], 0) == [1, 2, 3]

    def test_v3_none(self):
        assert rotate_v3(None, 2) is None


class TestMoveZeros:
    def test_basic(self):
        assert move_zeros([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]

    def test_no_zeros(self):
        assert move_zeros([1, 2, 3]) == [1, 2, 3]

    def test_all_zeros(self):
        assert move_zeros([0, 0, 0]) == [0, 0, 0]

    def test_empty(self):
        assert move_zeros([]) == []

    def test_bool_not_moved(self):
        result = move_zeros([0, 1, 0, 3, 12])
        assert result == [1, 3, 12, 0, 0]


class TestPlusOne:
    def test_v1_no_carry(self):
        assert plus_one_v1([1, 2, 3]) == [1, 2, 4]

    def test_v1_with_carry(self):
        assert plus_one_v1([1, 2, 9]) == [1, 3, 0]

    def test_v1_all_nines(self):
        assert plus_one_v1([9, 9, 9]) == [1, 0, 0, 0]

    def test_v2(self):
        assert plus_one_v2([1, 2, 3]) == [1, 2, 4]

    def test_v3(self):
        assert plus_one_v3([1, 2, 3]) == [1, 2, 4]


class TestMaxOnesIndex:
    def test_single_zero(self):
        assert max_ones_index([1, 0, 1]) == 1

    def test_zero_at_end(self):
        result = max_ones_index([1, 1, 0, 1, 1])
        assert result == 2

    def test_zero_at_start(self):
        result = max_ones_index([0, 1, 1, 1])
        assert result == 0


class TestLimit:
    def test_basic(self):
        assert limit([1, 2, 3, 4, 5], 2, 4) == [2, 3, 4]

    def test_no_limits(self):
        result = limit([3, 1, 2])
        assert sorted(result) == [1, 2, 3]

    def test_empty(self):
        assert limit([]) == []

    def test_min_only(self):
        assert limit([1, 2, 3, 4, 5], min_lim=3) == [3, 4, 5]


class TestThreeSum:
    def test_basic(self):
        result = three_sum([-1, 0, 1, 2, -1, -4])
        assert (-1, -1, 2) in result
        assert (-1, 0, 1) in result

    def test_no_solution(self):
        assert three_sum([1, 2, 3]) == set()

    def test_all_zeros(self):
        assert three_sum([0, 0, 0]) == {(0, 0, 0)}


class TestSummarizeRanges:
    def test_basic(self):
        assert summarize_ranges([0, 1, 2, 4, 5, 7]) == ["0-2", "4-5", "7"]

    def test_single(self):
        assert summarize_ranges([0]) == ["0"]

    def test_consecutive(self):
        assert summarize_ranges([0, 1, 2, 3]) == ["0-3"]


class TestMissingRanges:
    def test_basic(self):
        assert missing_ranges([0, 1, 3, 50, 75], 0, 99) == [(2, 2), (4, 49), (51, 74), (76, 99)]

    def test_no_missing(self):
        assert missing_ranges([0, 1, 2], 0, 2) == []

    def test_empty_arr(self):
        assert missing_ranges([], 1, 5) == [(1, 5)]


class TestTrimmean:
    def test_basic(self):
        result = trimmean([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 20)
        assert abs(result - 5.5) < 0.01


class TestTop1:
    def test_basic(self):
        assert top_1([1, 1, 2, 2, 3]) == [1, 2]

    def test_single_mode(self):
        assert top_1([1, 2, 2, 3]) == [2]

    def test_all_same(self):
        assert top_1([5, 5, 5]) == [5]


class TestDeleteNth:
    def test_basic(self):
        assert delete_nth([1, 2, 3, 1, 2, 1, 2, 3], 2) == [1, 2, 3, 1, 2, 3]

    def test_naive_same(self):
        arr = [1, 2, 3, 1, 2, 1]
        assert delete_nth(arr, 2) == delete_nth_naive(arr[:], 2)

    def test_n_zero(self):
        assert delete_nth([1, 2, 3], 0) == []

    def test_n_one(self):
        assert delete_nth([1, 1, 1], 1) == [1]
