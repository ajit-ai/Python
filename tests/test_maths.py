from algorithms.maths.gcd import gcd, lcm, trailing_zero, gcd_bit
from algorithms.maths.prime_check import prime_check
from algorithms.maths.pythagoras import pythagoras
from algorithms.maths.base_conversion import int_to_base, base_to_int
from algorithms.maths.power import power, power_recur
from algorithms.maths.combination import combination, combination_memo


class TestGcd:
    def test_basic(self):
        assert gcd(12, 8) == 4

    def test_coprime(self):
        assert gcd(7, 13) == 1

    def test_same(self):
        assert gcd(5, 5) == 5

    def test_lcm(self):
        assert lcm(4, 6) == 12

    def test_trailing_zero(self):
        assert trailing_zero(8) == 3

    def test_trailing_zero_odd(self):
        assert trailing_zero(7) == 0

    def test_gcd_bit(self):
        assert gcd_bit(12, 8) == 4

    def test_negative(self):
        assert gcd(-12, 8) == 4

    def test_zero_raises(self):
        import pytest
        with pytest.raises(ValueError):
            gcd(0, 5)


class TestPrimeCheck:
    def test_prime(self):
        assert prime_check(2) is True
        assert prime_check(3) is True
        assert prime_check(5) is True
        assert prime_check(7) is True
        assert prime_check(13) is True

    def test_not_prime(self):
        assert prime_check(1) is False
        assert prime_check(4) is False
        assert prime_check(9) is False

    def test_large_prime(self):
        assert prime_check(97) is True

    def test_negative(self):
        assert prime_check(-5) is False


class TestPythagoras:
    def test_find_hypotenuse(self):
        result = pythagoras(3, 4, "?")
        assert "5" in result

    def test_find_opposite(self):
        result = pythagoras("?", 4, 5)
        assert "3" in result

    def test_find_adjacent(self):
        result = pythagoras(3, "?", 5)
        assert "4" in result

    def test_already_known(self):
        assert pythagoras(3, 4, 5) == "You already know the answer!"


class TestBaseConversion:
    def test_int_to_base(self):
        assert int_to_base(10, 2) == "1010"
        assert int_to_base(255, 16) == "FF"
        assert int_to_base(0, 10) == "0"

    def test_base_to_int(self):
        assert base_to_int("1010", 2) == 10
        assert base_to_int("FF", 16) == 255

    def test_roundtrip(self):
        for num in range(100):
            for base in [2, 8, 10, 16]:
                assert base_to_int(int_to_base(num, base), base) == num

    def test_negative(self):
        assert int_to_base(-10, 2) == "-1010"


class TestPower:
    def test_basic(self):
        assert power(2, 10) == 1024

    def test_zero_exponent(self):
        assert power(5, 0) == 1

    def test_mod(self):
        assert power(2, 10, 1000) == 24

    def test_recur(self):
        assert power_recur(2, 10) == 1024

    def test_recur_mod(self):
        assert power_recur(2, 10, 1000) == 24


class TestCombination:
    def test_basic(self):
        assert combination(5, 2) == 10
        assert combination(10, 3) == 120

    def test_edge(self):
        assert combination(5, 0) == 1
        assert combination(5, 5) == 1

    def test_memo(self):
        assert combination_memo(5, 2) == 10
        assert combination_memo(10, 3) == 120

    def test_symmetry(self):
        for n in range(10):
            for r in range(n + 1):
                assert combination(n, r) == combination(n, n - r)
