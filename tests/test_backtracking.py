import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'algorithms', 'backtracking'))

from anagram import anagram, anagram2
from combination_sum import combination_sum
from generate_parenthesis import generate_parenthesis_v1, generate_parenthesis_v2
from letter_combination import letter_combinations
from permute import permute
from subsets import subsets, subsets_v2
from palindrome_partitioning import palindromic_substrings
from pattern_match import pattern_match


class TestAnagram:
    def test_anagram(self):
        assert anagram("abc", "bca") is True

    def test_not_anagram(self):
        assert anagram("abc", "def") is False

    def test_anagram2(self):
        assert anagram2("listen", "silent") is True

    def test_anagram2_different_length(self):
        assert anagram2("abc", "abcd") is False

    def test_empty(self):
        assert anagram("", "") is True


class TestCombinationSum:
    def test_basic(self):
        result = combination_sum([2, 3, 6, 7], 7)
        assert [2, 2, 3] in result
        assert [7] in result

    def test_no_solution(self):
        assert combination_sum([2], 3) == []

    def test_single_element(self):
        assert combination_sum([1], 3) == [[1, 1, 1]]


class TestGenerateParenthesis:
    def test_v1_n1(self):
        assert generate_parenthesis_v1(1) == ["()"]

    def test_v1_n2(self):
        result = generate_parenthesis_v1(2)
        assert "(())" in result
        assert "()()" in result

    def test_v2_n1(self):
        assert generate_parenthesis_v2(1) == ["()"]

    def test_v2_n2(self):
        result = generate_parenthesis_v2(2)
        assert "(())" in result
        assert "()()" in result

    def test_count_catalan(self):
        assert len(generate_parenthesis_v1(3)) == 5


class TestLetterCombinations:
    def test_basic(self):
        result = letter_combinations("23")
        assert "ad" in result
        assert "ae" in result
        assert "cf" in result
        assert len(result) == 9

    def test_single_digit(self):
        result = letter_combinations("2")
        assert result == ["a", "b", "c"]

    def test_empty(self):
        assert letter_combinations("") == []


class TestPermute:
    def test_basic(self):
        result = permute([1, 2, 3])
        assert len(result) == 6
        assert [1, 2, 3] in result
        assert [3, 2, 1] in result

    def test_single(self):
        assert permute([1]) == [[1]]

    def test_two(self):
        result = permute([1, 2])
        assert len(result) == 2


class TestSubsets:
    def test_basic(self):
        result = subsets([1, 2, 3])
        assert len(result) == 8
        assert [] in result
        assert [1, 2, 3] in result

    def test_v2(self):
        result = subsets_v2([1, 2, 3])
        assert len(result) == 8

    def test_empty(self):
        assert subsets([]) == [[]]

    def test_single(self):
        assert subsets([1]) == [[1], []]


class TestPalindromicSubstrings:
    def test_basic(self):
        result = palindromic_substrings("aab")
        assert ["a", "a", "b"] in result or ["aa", "b"] in result

    def test_single_char(self):
        assert palindromic_substrings("a") == [["a"]]

    def test_empty(self):
        assert palindromic_substrings("") == [[]]


class TestPatternMatch:
    def test_match(self):
        assert pattern_match("abba", "redbluebluered") is True

    def test_no_match(self):
        assert pattern_match("aabb", "xyzxyz") is False

    def test_single_char(self):
        assert pattern_match("a", "hello") is True
