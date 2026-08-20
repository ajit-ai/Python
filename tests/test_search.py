import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'algorithms', 'search'))

from binary_search import binary_search, binary_search_recur
from linear_search import linear_search


class TestBinarySearch:
    def test_found(self):
        assert binary_search([1, 2, 3, 4, 5], 3) == 2

    def test_not_found(self):
        assert binary_search([1, 2, 3, 4, 5], 6) is None

    def test_first(self):
        assert binary_search([1, 2, 3, 4, 5], 1) == 0

    def test_last(self):
        assert binary_search([1, 2, 3, 4, 5], 5) == 4

    def test_single(self):
        assert binary_search([1], 1) == 0

    def test_recur(self):
        assert binary_search_recur([1, 2, 3, 4, 5], 0, 4, 3) == 2

    def test_recur_not_found(self):
        assert binary_search_recur([1, 2, 3, 4, 5], 0, 4, 6) == -1


class TestLinearSearch:
    def test_found(self):
        assert linear_search([5, 3, 7, 1, 9], 7) == 2

    def test_not_found(self):
        assert linear_search([5, 3, 7, 1, 9], 2) == -1

    def test_first(self):
        assert linear_search([5, 3, 7, 1, 9], 5) == 0

    def test_single(self):
        assert linear_search([1], 1) == 0
