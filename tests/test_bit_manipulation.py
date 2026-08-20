from algorithms.bit_manipulation.add_bitwise_operator import add_bitwise_operator
from algorithms.bit_manipulation.binary_gap import binary_gap, binary_gap_improved
from algorithms.bit_manipulation.bit_operation import get_bit, set_bit, clear_bit, update_bit
from algorithms.bit_manipulation.count_flips_to_convert import count_flips_to_convert
from algorithms.bit_manipulation.count_ones import count_ones_recur, count_ones_iter
from algorithms.bit_manipulation.find_missing_number import find_missing_number, find_missing_number2
from algorithms.bit_manipulation.power_of_two import is_power_of_two
from algorithms.bit_manipulation.reverse_bits import reverse_bits
from algorithms.bit_manipulation.single_number import single_number
from algorithms.bit_manipulation.has_alternative_bit import has_alternative_bit, has_alternative_bit_fast
from algorithms.bit_manipulation.swap_pair import swap_pair


class TestAddBitwiseOperator:
    def test_basic(self):
        assert add_bitwise_operator(5, 3) == 8

    def test_zero(self):
        assert add_bitwise_operator(0, 5) == 5

    def test_large(self):
        assert add_bitwise_operator(100, 200) == 300

    def test_same(self):
        assert add_bitwise_operator(7, 7) == 14


class TestBinaryGap:
    def test_basic(self):
        assert binary_gap(9) == 3

    def test_single_one(self):
        assert binary_gap(1) == 0

    def test_zero(self):
        assert binary_gap(0) == 0

    def test_improved(self):
        result = binary_gap_improved(9)
        assert result >= 1


class TestBitOperation:
    def test_get_bit(self):
        assert get_bit(6, 1) is True
        assert get_bit(6, 2) is True
        assert get_bit(6, 0) is False

    def test_set_bit(self):
        assert set_bit(4, 0) == 5

    def test_clear_bit(self):
        assert clear_bit(7, 1) == 5

    def test_update_bit(self):
        assert update_bit(5, 1, 1) == 7
        assert update_bit(7, 1, 0) == 5


class TestCountFlipsToConvert:
    def test_basic(self):
        assert count_flips_to_convert(10, 20) == 4

    def test_same(self):
        assert count_flips_to_convert(5, 5) == 0

    def test_zero_to_one(self):
        assert count_flips_to_convert(0, 1) == 1


class TestCountOnes:
    def test_recur(self):
        assert count_ones_recur(7) == 3

    def test_iter(self):
        assert count_ones_iter(7) == 3

    def test_zero(self):
        assert count_ones_recur(0) == 0
        assert count_ones_iter(0) == 0

    def test_power_of_two(self):
        assert count_ones_iter(16) == 1


class TestFindMissingNumber:
    def test_basic(self):
        assert find_missing_number([0, 1, 3]) == 2

    def test_v2(self):
        assert find_missing_number2([0, 1, 3]) == 2

    def test_first_missing(self):
        assert find_missing_number([1, 2, 3]) == 0

    def test_last_missing(self):
        assert find_missing_number([0, 1, 2]) == 3


class TestPowerOfTwo:
    def test_power(self):
        assert is_power_of_two(16) is True
        assert is_power_of_two(1) is True

    def test_not_power(self):
        assert is_power_of_two(18) is False
        assert is_power_of_two(0) is False

    def test_negative(self):
        assert is_power_of_two(-4) is False


class TestReverseBits:
    def test_basic(self):
        assert reverse_bits(1) == 2147483648

    def test_zero(self):
        assert reverse_bits(0) == 0

    def test_all_ones(self):
        assert reverse_bits(4294967295) == 4294967295


class TestSingleNumber:
    def test_basic(self):
        assert single_number([2, 2, 1]) == 1

    def test_longer(self):
        assert single_number([4, 1, 2, 1, 2]) == 4


class TestHasAlternativeBit:
    def test_alternating(self):
        assert has_alternative_bit(5) is True
        assert has_alternative_bit(10) is True

    def test_not_alternating(self):
        assert has_alternative_bit(7) is False

    def test_fast(self):
        assert has_alternative_bit_fast(5) is True


class TestSwapPair:
    def test_basic(self):
        assert swap_pair(1) == 2
        assert swap_pair(2) == 1

    def test_zero(self):
        assert swap_pair(0) == 0
