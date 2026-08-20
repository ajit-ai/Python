from algorithms.dynamic_programming.coin_change import count as coin_count
from algorithms.dynamic_programming.edit_distance import edit_distance
from algorithms.dynamic_programming.knapsack import Item, get_maximum_value
from algorithms.dynamic_programming.max_subarray import max_subarray
from algorithms.dynamic_programming.climbing_down_stairs import climb_stairs, climb_stairs_optimized
from algorithms.dynamic_programming.longest_common_subsequence import longest_common_subsequence
from algorithms.dynamic_programming.longest_increasing import longest_increasing_subsequence
from algorithms.dynamic_programming.buy_sell_stock import max_profit_naive, max_profit_optimized


class TestCoinChange:
    def test_basic(self):
        assert coin_count([1, 2, 5], 5) == 4

    def test_single_coin(self):
        assert coin_count([1], 5) == 1

    def test_impossible(self):
        assert coin_count([2], 3) == 0

    def test_zero(self):
        assert coin_count([1, 2], 0) == 1


class TestEditDistance:
    def test_basic(self):
        assert edit_distance("kitten", "sitting") == 3

    def test_same(self):
        assert edit_distance("abc", "abc") == 0

    def test_empty(self):
        assert edit_distance("", "abc") == 3

    def test_both_empty(self):
        assert edit_distance("", "") == 0


class TestKnapsack:
    def test_basic(self):
        items = [Item(60, 10), Item(100, 20), Item(120, 30)]
        assert get_maximum_value(items, 50) == 220

    def test_single_item(self):
        items = [Item(50, 10)]
        assert get_maximum_value(items, 10) == 50

    def test_no_capacity(self):
        items = [Item(60, 10)]
        assert get_maximum_value(items, 0) == 0


class TestMaxSubarray:
    def test_basic(self):
        assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

    def test_all_positive(self):
        assert max_subarray([1, 2, 3]) == 6

    def test_all_negative(self):
        assert max_subarray([-3, -2, -1]) == -1

    def test_single(self):
        assert max_subarray([5]) == 5


class TestClimbStairs:
    def test_basic(self):
        assert climb_stairs(2) == 2
        assert climb_stairs(3) == 3

    def test_optimized(self):
        assert climb_stairs_optimized(2) == 2
        assert climb_stairs_optimized(3) == 3

    def test_one(self):
        assert climb_stairs(1) == 1

    def test_large(self):
        assert climb_stairs(10) == 89


class TestLongestCommonSubsequence:
    def test_basic(self):
        assert longest_common_subsequence("abcde", "ace") == 3

    def test_no_common(self):
        assert longest_common_subsequence("abc", "def") == 0

    def test_identical(self):
        assert longest_common_subsequence("abc", "abc") == 3

    def test_empty(self):
        assert longest_common_subsequence("", "abc") == 0


class TestLongestIncreasingSubsequence:
    def test_basic(self):
        assert longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]) == 4

    def test_sorted(self):
        assert longest_increasing_subsequence([1, 2, 3, 4, 5]) == 5

    def test_reverse(self):
        assert longest_increasing_subsequence([5, 4, 3, 2, 1]) == 1


class TestBuySellStock:
    def test_naive(self):
        assert max_profit_naive([7, 1, 5, 3, 6, 4]) == 5

    def test_optimized(self):
        assert max_profit_optimized([7, 1, 5, 3, 6, 4]) == 5

    def test_no_profit(self):
        assert max_profit_naive([7, 6, 4, 3, 1]) == 0
        assert max_profit_optimized([7, 6, 4, 3, 1]) == 0

    def test_single_price(self):
        assert max_profit_optimized([5]) == 0
