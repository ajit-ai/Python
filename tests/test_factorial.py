import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'algorithms', 'factorial'))

from factorial import get_recursive_factorial, get_iterative_factorial


class TestFactorial:
    def test_recursive_zero(self):
        assert get_recursive_factorial(0) == 1

    def test_recursive_one(self):
        assert get_recursive_factorial(1) == 1

    def test_recursive_five(self):
        assert get_recursive_factorial(5) == 120

    def test_recursive_ten(self):
        assert get_recursive_factorial(10) == 3628800

    def test_iterative_zero(self):
        assert get_iterative_factorial(0) == 1

    def test_iterative_five(self):
        assert get_iterative_factorial(5) == 120

    def test_iterative_ten(self):
        assert get_iterative_factorial(10) == 3628800

    def test_negative_recursive(self):
        assert get_recursive_factorial(-1) == -1

    def test_negative_iterative(self):
        assert get_iterative_factorial(-1) == -1

    def test_both_methods_agree(self):
        for n in range(10):
            assert get_recursive_factorial(n) == get_iterative_factorial(n)
