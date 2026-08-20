import pytest

from algorithms.dynamic_programming.longest_palindrome import (
    longest_palindrome_substring,
    longest_palindrome_subsequence,
)
from algorithms.dynamic_programming.house_robber import house_robber, house_robber_circular
from algorithms.dynamic_programming.unique_paths import unique_paths, unique_paths_with_obstacles
from algorithms.dynamic_programming.subset_sum import subset_sum, subset_sum_count
from algorithms.dynamic_programming.word_break import word_break, word_break_all
from algorithms.dynamic_programming.egg_dropping import egg_drop
from algorithms.dynamic_programming.rod_cutting import rod_cutting
from algorithms.dynamic_programming.maximum_sum_non_adjacent import rob

from algorithms.strings.kmp_search import kmp_search
from algorithms.strings.rabin_karp import rabin_karp

from algorithms.sort.heap_sort import heap_sort
from algorithms.sort.radix_sort import radix_sort
from algorithms.sort.bucket_sort import bucket_sort

from algorithms.search.ternary_search import ternary_search, ternary_search_recursive

from algorithms.maths.sieve_of_eratosthenes import sieve_of_eratosthenes
from algorithms.maths.fibonacci import fibonacci, fibonacci_iterative, fibonacci_matrix
from algorithms.maths.modular_inverse import modular_inverse, extended_gcd

from algorithms.arrays.max_product_subarray import max_product_subarray
from algorithms.arrays.product_except_self import product_except_self
from algorithms.arrays.dutch_national_flag import dutch_national_flag


class TestLongestPalindrome:
    def test_single_char_string(self):
        assert longest_palindrome_substring("a") == "a"

    def test_two_char_string(self):
        result = longest_palindrome_substring("bb")
        assert result == "bb"

    def test_classic_odd_palindrome(self):
        assert longest_palindrome_substring("babad") in ("bab", "aba")

    def test_even_palindrome(self):
        assert longest_palindrome_substring("cbbd") == "bb"

    def test_entire_string_is_palindrome(self):
        assert longest_palindrome_substring("racecar") == "racecar"

    def test_subsequence_basic(self):
        assert longest_palindrome_subsequence("bbbab") == 4

    def test_subsequence_all_same(self):
        assert longest_palindrome_subsequence("aaaa") == 4

    def test_subsequence_no_repeats(self):
        assert longest_palindrome_subsequence("abcde") == 1

    def test_subsequence_classic(self):
        assert longest_palindrome_subsequence("aebcbda") == 5


class TestHouseRobber:
    def test_empty(self):
        assert house_robber([]) == 0

    def test_single_house(self):
        assert house_robber([5]) == 5

    def test_two_houses(self):
        assert house_robber([1, 2]) == 2

    def test_classic_example(self):
        assert house_robber([1, 2, 3, 1]) == 4

    def test_alternating(self):
        assert house_robber([2, 7, 9, 3, 1]) == 12

    def test_circular_single(self):
        assert house_robber_circular([5]) == 5

    def test_circular_three(self):
        assert house_robber_circular([1, 2, 3]) == 3

    def test_circular_classic(self):
        assert house_robber_circular([2, 3, 2]) == 3

    def test_circular_bigger(self):
        assert house_robber_circular([1, 2, 3, 1]) == 4


class TestUniquePaths:
    def test_single_cell(self):
        assert unique_paths(1, 1) == 1

    def test_one_row(self):
        assert unique_paths(1, 5) == 1

    def test_one_column(self):
        assert unique_paths(5, 1) == 1

    def test_3x3(self):
        assert unique_paths(3, 3) == 6

    def test_3x7(self):
        assert unique_paths(3, 7) == 28

    def test_no_obstacles(self):
        grid = [[0] * 3 for _ in range(3)]
        assert unique_paths_with_obstacles(grid) == 6

    def test_obstacle_in_middle(self):
        grid = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0],
        ]
        assert unique_paths_with_obstacles(grid) == 2

    def test_obstacle_at_start(self):
        grid = [[1, 0], [0, 0]]
        assert unique_paths_with_obstacles(grid) == 0

    def test_obstacle_at_end(self):
        grid = [[0, 0], [0, 1]]
        assert unique_paths_with_obstacles(grid) == 0


class TestSubsetSum:
    def test_empty_set_zero_target(self):
        assert subset_sum([], 0) is True

    def test_single_match(self):
        assert subset_sum([3], 3) is True

    def test_no_match(self):
        assert subset_sum([1, 2], 5) is False

    def test_classic(self):
        assert subset_sum([3, 34, 4, 12, 5, 2], 9) is True

    def test_negative_target(self):
        assert subset_sum([1, 2, 3], -1) is False

    def test_count_basic(self):
        assert subset_sum_count([1, 2, 3], 3) == 2

    def test_count_no_match(self):
        assert subset_sum_count([1, 2], 10) == 0

    def test_count_duplicates(self):
        assert subset_sum_count([1, 1, 1], 2) == 3


class TestWordBreak:
    def test_simple_match(self):
        assert word_break("leetcode", ["leet", "code"]) is True

    def test_no_match(self):
        assert word_break("catsandog", ["cats", "dog", "sand"]) is False

    def test_entire_dict(self):
        assert word_break("applepenapple", ["apple", "pen"]) is True

    def test_empty_string(self):
        assert word_break("", ["a"]) is True

    def test_all_words_found(self):
        result = word_break_all("catsandog", ["cats", "dog", "sand", "cat"])
        assert isinstance(result, list)

    def test_word_break_all_basic(self):
        result = word_break_all("abc", ["a", "b", "c"])
        assert ["a", "b", "c"] in result

    def test_word_break_all_no_match(self):
        assert word_break_all("xyz", ["a", "b"]) == []

    def test_word_break_all_single(self):
        result = word_break_all("abc", ["abc"])
        assert ["abc"] in result


class TestEggDropping:
    def test_one_egg_one_floor(self):
        assert egg_drop(1, 1) == 1

    def test_one_egg_multiple_floors(self):
        assert egg_drop(1, 10) == 10

    def test_multiple_eggs_one_floor(self):
        assert egg_drop(2, 1) == 1

    def test_two_eggs_two_floors(self):
        assert egg_drop(2, 2) == 2

    def test_classic_2_10(self):
        assert egg_drop(2, 10) == 4

    def test_classic_2_6(self):
        assert egg_drop(2, 6) == 3


class TestRodCutting:
    def test_length_zero(self):
        assert rod_cutting([], 0) == 0

    def test_single_cut(self):
        assert rod_cutting([5], 1) == 5

    def test_two_cuts(self):
        assert rod_cutting([1, 5, 8, 10], 4) == 10

    def test_classic(self):
        assert rod_cutting([1, 5, 8, 9, 10, 17, 17, 20], 8) == 22

    def test_all_same_price(self):
        assert rod_cutting([3, 3, 3], 3) == 9


class TestMaxSumNonAdjacent:
    def test_empty(self):
        assert rob([]) == 0

    def test_single(self):
        assert rob([5]) == 5

    def test_two_elements(self):
        assert rob([1, 2]) == 2

    def test_classic(self):
        assert rob([2, 7, 9, 3, 1]) == 12

    def test_all_negative(self):
        assert rob([-1, -2, -3]) == -1

    def test_alternating(self):
        assert rob([1, 3, 1, 3, 100]) == 103


class TestKMP:
    def test_simple_match(self):
        assert kmp_search("ababcabcababc", "abc") == [2, 5, 10]

    def test_no_match(self):
        assert kmp_search("abcdef", "xyz") == []

    def test_full_match(self):
        assert kmp_search("aaa", "aaa") == [0]

    def test_single_char(self):
        assert kmp_search("aaaa", "a") == [0, 1, 2, 3]

    def test_pattern_longer_than_text(self):
        assert kmp_search("ab", "abcd") == []

    def test_repeated_pattern(self):
        assert kmp_search("aaaa", "aa") == [0, 1, 2]

    def test_empty_pattern(self):
        assert kmp_search("abc", "") == []


class TestRabinKarp:
    def test_simple_match(self):
        assert rabin_karp("ababcabcababc", "abc") == [2, 5, 10]

    def test_no_match(self):
        assert rabin_karp("abcdef", "xyz") == []

    def test_full_match(self):
        assert rabin_karp("aaa", "aaa") == [0]

    def test_single_char(self):
        assert rabin_karp("aaaa", "a") == [0, 1, 2, 3]

    def test_pattern_longer_than_text(self):
        assert rabin_karp("ab", "abcd") == []

    def test_repeated_pattern(self):
        assert rabin_karp("aaaa", "aa") == [0, 1, 2]


class TestHeapSort:
    def test_empty(self):
        assert heap_sort([]) == []

    def test_single(self):
        assert heap_sort([5]) == [5]

    def test_sorted(self):
        assert heap_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_reverse(self):
        assert heap_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_duplicates(self):
        assert heap_sort([3, 1, 2, 3, 1]) == [1, 1, 2, 3, 3]

    def test_negatives(self):
        assert heap_sort([-3, -1, -2]) == [-3, -2, -1]

    def test_mixed(self):
        assert heap_sort([3, -1, 4, -2, 0]) == [-2, -1, 0, 3, 4]


class TestRadixSort:
    def test_empty(self):
        assert radix_sort([]) == []

    def test_single(self):
        assert radix_sort([5]) == [5]

    def test_sorted(self):
        assert radix_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_reverse(self):
        assert radix_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_duplicates(self):
        assert radix_sort([3, 1, 2, 3, 1]) == [1, 1, 2, 3, 3]

    def test_large_numbers(self):
        assert radix_sort([170, 45, 75, 90, 802, 24, 2, 66]) == [2, 24, 45, 66, 75, 90, 170, 802]

    def test_in_place_returns_arr(self):
        arr = [5, 3, 1]
        result = radix_sort(arr)
        assert result == [1, 3, 5]
        assert isinstance(result, list)


class TestBucketSort:
    def test_empty(self):
        assert bucket_sort([]) == []

    def test_single(self):
        assert bucket_sort([5]) == [5]

    def test_sorted(self):
        assert bucket_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_reverse(self):
        assert bucket_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_duplicates(self):
        assert bucket_sort([3, 1, 2, 3, 1]) == [1, 1, 2, 3, 3]

    def test_floats(self):
        assert bucket_sort([0.42, 0.32, 0.23, 0.52, 0.25, 0.47]) == [
            0.23, 0.25, 0.32, 0.42, 0.47, 0.52
        ]


class TestTernarySearch:
    def test_found(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert ternary_search(arr, 5) == 4

    def test_not_found(self):
        arr = [1, 2, 3, 4, 5]
        assert ternary_search(arr, 10) == -1

    def test_first_element(self):
        arr = [1, 2, 3, 4, 5]
        assert ternary_search(arr, 1) == 0

    def test_last_element(self):
        arr = [1, 2, 3, 4, 5]
        assert ternary_search(arr, 5) == 4

    def test_recursive_found(self):
        arr = [10, 20, 30, 40, 50]
        assert ternary_search_recursive(arr, 30) == 2

    def test_recursive_not_found(self):
        arr = [10, 20, 30, 40, 50]
        assert ternary_search_recursive(arr, 25) == -1

    def test_recursive_single(self):
        assert ternary_search_recursive([5], 5) == 0

    def test_recursive_empty(self):
        assert ternary_search_recursive([], 1) == -1


class TestSieve:
    def test_small(self):
        assert sieve_of_eratosthenes(10) == [2, 3, 5, 7]

    def test_two(self):
        assert sieve_of_eratosthenes(2) == [2]

    def test_one(self):
        assert sieve_of_eratosthenes(1) == []

    def test_twenty(self):
        assert sieve_of_eratosthenes(20) == [2, 3, 5, 7, 11, 13, 17, 19]

    def test_zero(self):
        assert sieve_of_eratosthenes(0) == []

    def test_hundred_count(self):
        assert len(sieve_of_eratosthenes(100)) == 25


class TestFibonacci:
    def test_zero(self):
        assert fibonacci(0) == []

    def test_one(self):
        assert fibonacci(1) == [0]

    def test_two(self):
        assert fibonacci(2) == [0, 1]

    def test_ten(self):
        result = fibonacci(10)
        assert result == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    def test_iterative(self):
        assert fibonacci_iterative(5) == [0, 1, 1, 2, 3]

    def test_iterative_one(self):
        assert fibonacci_iterative(1) == [0]

    def test_matrix(self):
        assert fibonacci_matrix(5) == [0, 1, 1, 2, 3]

    def test_matrix_ten(self):
        assert fibonacci_matrix(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    def test_all_methods_agree(self):
        assert fibonacci(15) == fibonacci_iterative(15) == fibonacci_matrix(15)


class TestModularInverse:
    def test_basic(self):
        assert modular_inverse(3, 11) == 4

    def test_result_valid(self):
        a, m = 7, 13
        inv = modular_inverse(a, m)
        assert (a * inv) % m == 1

    def test_one(self):
        assert modular_inverse(1, 5) == 1

    def test_no_inverse(self):
        assert modular_inverse(2, 4) is None

    def test_extended_gcd_basic(self):
        assert extended_gcd(35, 15) == (5, 1, -2)

    def test_extended_gcd_coprime(self):
        result = extended_gcd(3, 7)
        assert result[0] == 1

    def test_extended_gcd_zero(self):
        assert extended_gcd(0, 5) == (5, 0, 1)

    def test_extended_gcd_both_equal(self):
        assert extended_gcd(7, 7) == (7, 1, 0)


class TestMaxProduct:
    def test_single(self):
        assert max_product_subarray([2]) == 2

    def test_two_positives(self):
        assert max_product_subarray([2, 3]) == 6

    def test_classic(self):
        assert max_product_subarray([2, 3, -2, 4]) == 6

    def test_negative(self):
        assert max_product_subarray([-2, 0, -1]) == 0

    def test_two_negatives(self):
        assert max_product_subarray([-2, -3, -2]) == 6

    def test_zeros(self):
        assert max_product_subarray([0, 2]) == 2

    def test_mixed(self):
        assert max_product_subarray([-2, 3, -4]) == 24


class TestProductExceptSelf:
    def test_basic(self):
        assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]

    def test_with_zero(self):
        assert product_except_self([1, 2, 0, 4]) == [0, 0, 8, 0]

    def test_two_elements(self):
        assert product_except_self([3, 4]) == [4, 3]

    def test_two_zeros(self):
        assert product_except_self([0, 0]) == [0, 0]

    def test_negative(self):
        assert product_except_self([-1, -2, -3]) == [6, 3, 2]

    def test_with_one(self):
        assert product_except_self([1, 1, 1, 1]) == [1, 1, 1, 1]

    def test_preserves_length(self):
        assert len(product_except_self([1, 2, 3, 4, 5])) == 5


class TestDutchFlag:
    def test_basic(self):
        arr = [2, 0, 1]
        dutch_national_flag(arr)
        assert arr == [0, 1, 2]

    def test_all_zeros(self):
        arr = [0, 0, 0]
        dutch_national_flag(arr)
        assert arr == [0, 0, 0]

    def test_all_ones(self):
        arr = [1, 1, 1]
        dutch_national_flag(arr)
        assert arr == [1, 1, 1]

    def test_all_twos(self):
        arr = [2, 2, 2]
        dutch_national_flag(arr)
        assert arr == [2, 2, 2]

    def test_empty(self):
        arr = []
        dutch_national_flag(arr)
        assert arr == []

    def test_single(self):
        arr = [1]
        dutch_national_flag(arr)
        assert arr == [1]

    def test_sorted_descending(self):
        arr = [2, 2, 1, 1, 0, 0]
        dutch_national_flag(arr)
        assert arr == [0, 0, 1, 1, 2, 2]
