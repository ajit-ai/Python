from algorithms.map.is_anagram import is_anagram
from algorithms.map.is_isomorphic import is_isomorphic


class TestIsAnagram:
    def test_anagram(self):
        assert is_anagram("listen", "silent") is True

    def test_not_anagram(self):
        assert is_anagram("hello", "world") is False

    def test_same_word(self):
        assert is_anagram("test", "test") is True

    def test_empty(self):
        assert is_anagram("", "") is True

    def test_different_length(self):
        assert is_anagram("abc", "abcd") is False

    def test_case_sensitive(self):
        assert is_anagram("Listen", "Silent") is False


class TestIsIsomorphic:
    def test_isomorphic(self):
        assert is_isomorphic("egg", "add") is True

    def test_not_isomorphic(self):
        assert is_isomorphic("foo", "bar") is False

    def test_same(self):
        assert is_isomorphic("aab", "xxy") is True

    def test_different_length(self):
        assert is_isomorphic("ab", "abc") is False

    def test_single(self):
        assert is_isomorphic("a", "b") is True
