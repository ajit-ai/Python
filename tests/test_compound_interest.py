import math
from functools import reduce


def compound_interest_1(p, r, n, t):
    return p * (1 + r/n) ** (n*t)

def compound_interest_2(p, r, n, t):
    amount = p
    for _ in range(n * t):
        amount *= (1 + r/n)
    return amount

def compound_interest_3(p, r, n, t):
    if t == 0:
        return p
    return compound_interest_3(p * (1 + r/n) ** n, r, n, t-1)

def compound_interest_4(p, r, n, t):
    return p * math.pow((1 + r/n), n*t)

def compound_interest_5(p, r, n, t):
    return reduce(lambda acc, _: acc * (1 + r/n), range(n*t), p)


class TestCompoundInterest:
    def test_basic(self):
        result = compound_interest_1(1000, 0.05, 1, 1)
        assert abs(result - 1050.0) < 0.01

    def test_multiple_compoundings(self):
        result = compound_interest_1(1000, 0.10, 4, 3)
        assert abs(result - 1344.8888) < 1

    def test_zero_time(self):
        assert compound_interest_3(1000, 0.05, 1, 0) == 1000

    def test_methods_agree(self):
        p, r, n, t = 1000, 0.05, 12, 5
        r1 = compound_interest_1(p, r, n, t)
        r2 = compound_interest_2(p, r, n, t)
        r4 = compound_interest_4(p, r, n, t)
        r5 = compound_interest_5(p, r, n, t)
        assert abs(r1 - r2) < 0.01
        assert abs(r1 - r4) < 0.01
        assert abs(r1 - r5) < 0.01

    def test_negative_rate(self):
        result = compound_interest_1(1000, -0.05, 1, 1)
        assert result < 1000

    def test_large_time(self):
        result = compound_interest_1(100, 0.10, 1, 30)
        assert result > 1000
