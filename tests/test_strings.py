from algorithms.strings.fizzbuzz import fizzbuzz, fizzbuzz_with_helper_func
from algorithms.strings.is_palindrome import is_palindrome, is_palindrome_reverse, remove_punctuation, string_reverse
from algorithms.strings.caesar_cipher import caesar_cipher
from algorithms.strings.check_pangram import check_pangram
from algorithms.strings.atbash_cipher import atbash
from algorithms.strings.longest_common_prefix import longest_common_prefix_v1, longest_common_prefix_v2
from algorithms.strings.reverse_string import recursive, iterative, pythonic, ultra_pythonic
from algorithms.strings.group_anagrams import group_anagrams
from algorithms.strings.first_unique_char import first_unique_char
from algorithms.strings.int_to_roman import int_to_roman
from algorithms.strings.roman_to_int import roman_to_int
from algorithms.strings.reverse_vowel import reverse_vowel
from algorithms.strings.reverse_words import reverse_words


class TestFizzBuzz:
    def test_basic(self):
        result = fizzbuzz(5)
        assert result[0] == 1
        assert result[1] == 2
        assert result[2] == "Fizz"
        assert result[3] == 4
        assert result[4] == "Buzz"

    def test_fizzbuzz(self):
        result = fizzbuzz(15)
        assert result[14] == "FizzBuzz"

    def test_helper_func(self):
        result = fizzbuzz_with_helper_func(5)
        assert result[2] == "Fizz"
        assert result[4] == "Buzz"

    def test_invalid(self):
        import pytest
        with pytest.raises(ValueError):
            fizzbuzz(0)


class TestIsPalindrome:
    def test_simple(self):
        assert is_palindrome("racecar") is True

    def test_with_spaces(self):
        assert is_palindrome("A man, a plan, a canal: Panama") is True

    def test_not_palindrome(self):
        assert is_palindrome("hello") is False

    def test_remove_punctuation(self):
        assert remove_punctuation("A man, a plan!") == "amanaplan"

    def test_string_reverse(self):
        assert string_reverse("hello") == "olleh"

    def test_reverse_palindrome(self):
        assert is_palindrome_reverse("racecar") is True

    def test_single_char(self):
        assert is_palindrome("a") is True

    def test_empty(self):
        assert is_palindrome("") is True


class TestCaesarCipher:
    def test_encrypt(self):
        assert caesar_cipher("abc", 3) == "def"

    def test_wrap(self):
        assert caesar_cipher("xyz", 3) == "abc"

    def test_mixed(self):
        assert caesar_cipher("Hello, World!", 5) == "Mjqqt, Btwqi!"

    def test_zero_shift(self):
        assert caesar_cipher("abc", 0) == "abc"

    def test_full_rotation(self):
        assert caesar_cipher("abc", 26) == "abc"


class TestCheckPangram:
    def test_pangram(self):
        assert check_pangram("The quick brown fox jumps over the lazy dog") is True

    def test_not_pangram(self):
        assert check_pangram("Hello World") is False

    def test_all_letters(self):
        assert check_pangram("abcdefghijklmnopqrstuvwxyz") is True


class TestAtbashCipher:
    def test_basic(self):
        assert atbash("abc") == "zyx"

    def test_mixed(self):
        assert atbash("Hello") == "Svool"

    def test_numbers(self):
        assert atbash("123") == "123"

    def test_uppercase(self):
        assert atbash("ABC") == "ZYX"


class TestLongestCommonPrefix:
    def test_v1(self):
        assert longest_common_prefix_v1(["flower", "flow", "flight"]) == "fl"

    def test_v1_no_common(self):
        assert longest_common_prefix_v1(["dog", "racecar", "car"]) == ""

    def test_v2(self):
        assert longest_common_prefix_v2(["flower", "flow", "flight"]) == "fl"

    def test_single(self):
        assert longest_common_prefix_v1(["hello"]) == "hello"

    def test_empty(self):
        assert longest_common_prefix_v1([]) == ""


class TestReverseString:
    def test_recursive(self):
        assert recursive("hello") == "olleh"

    def test_iterative(self):
        assert iterative("hello") == "olleh"

    def test_pythonic(self):
        assert pythonic("hello") == "olleh"

    def test_ultra_pythonic(self):
        assert ultra_pythonic("hello") == "olleh"

    def test_empty(self):
        assert recursive("") == ""

    def test_single(self):
        assert recursive("a") == "a"


class TestGroupAnagrams:
    def test_basic(self):
        result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        assert len(result) == 3

    def test_single(self):
        result = group_anagrams(["hello"])
        assert len(result) == 1


class TestFirstUniqueChar:
    def test_basic(self):
        assert first_unique_char("leetcode") == 0

    def test_not_found(self):
        assert first_unique_char("aabb") == -1

    def test_single(self):
        assert first_unique_char("z") == 0


class TestIntToRoman:
    def test_basic(self):
        assert int_to_roman(3) == "III"
        assert int_to_roman(4) == "IV"
        assert int_to_roman(9) == "IX"
        assert int_to_roman(58) == "LVIII"
        assert int_to_roman(1994) == "MCMXCIV"


class TestRomanToInt:
    def test_basic(self):
        assert roman_to_int("III") == 3
        assert roman_to_int("IV") == 4
        assert roman_to_int("IX") == 9
        assert roman_to_int("LVIII") == 58
        assert roman_to_int("MCMXCIV") == 1994


class TestReverseVowel:
    def test_basic(self):
        assert reverse_vowel("hello") == "holle"

    def test_all_vowels(self):
        assert reverse_vowel("aeiou") == "uoiea"

    def test_no_vowels(self):
        assert reverse_vowel("xyz") == "xyz"


class TestReverseWords:
    def test_basic(self):
        assert reverse_words("the sky is blue") == "blue is sky the"

    def test_spaces(self):
        assert reverse_words("  hello world  ") == "world hello"

    def test_single(self):
        assert reverse_words("hello") == "hello"
