import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'algorithms', 'compression'))

from rle_compression import encode_rle, decode_rle
from elias import (elias_gamma_encode, elias_gamma_decode,
                   elias_delta_encode, elias_delta_decode)


class TestRLECompression:
    def test_encode(self):
        assert encode_rle("AAABBBCCD") == "3A3B2C1D"

    def test_decode(self):
        assert decode_rle("3A3B2C1D") == "AAABBBCCD"

    def test_roundtrip(self):
        original = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
        encoded = encode_rle(original)
        assert decode_rle(encoded) == original

    def test_single_char(self):
        assert encode_rle("A") == "1A"

    def test_empty(self):
        assert encode_rle("") == ""

    def test_decode_single(self):
        assert decode_rle("5A") == "AAAAA"


class TestEliasGamma:
    def test_encode(self):
        assert elias_gamma_encode(1) == "1"
        assert elias_gamma_encode(2) == "010"
        assert elias_gamma_encode(3) == "011"

    def test_decode(self):
        assert elias_gamma_decode("1") == 1
        assert elias_gamma_decode("010") == 2
        assert elias_gamma_decode("011") == 3

    def test_roundtrip(self):
        for n in range(1, 50):
            encoded = elias_gamma_encode(n)
            assert elias_gamma_decode(encoded) == n

    def test_invalid(self):
        import pytest
        with pytest.raises(ValueError):
            elias_gamma_encode(0)
        with pytest.raises(ValueError):
            elias_gamma_decode("")


class TestEliasDelta:
    def test_encode(self):
        assert elias_delta_encode(1) == "1"
        assert elias_delta_encode(2) == "0100"

    def test_decode(self):
        assert elias_delta_decode("1") == 1
        assert elias_delta_decode("0100") == 2

    def test_roundtrip(self):
        for n in range(1, 50):
            encoded = elias_delta_encode(n)
            assert elias_delta_decode(encoded) == n

    def test_invalid(self):
        import pytest
        with pytest.raises(ValueError):
            elias_delta_encode(0)
        with pytest.raises(ValueError):
            elias_delta_decode("")
