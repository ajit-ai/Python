import pandas as pd
import math
from functools import reduce
import numpy as np
from decimal import Decimal, getcontext


# 1. Using a simple formula
def compound_interest_1(p, r, n, t):
    return p * (1 + r/n) ** (n*t)


print(compound_interest_1(1000, 0.05, 4, 5))  # Quarterly compounding


# 2. Using a for loop
def compound_interest_2(p, r, n, t):
    amount = p
    for _ in range(n * t):
        amount *= (1 + r/n)
    return amount


print(compound_interest_2(1000, 0.05, 4, 5))


# 3. Using recursion
def compound_interest_3(p, r, n, t):
    if t == 0:
        return p
    return compound_interest_3(p * (1 + r/n) ** n, r, n, t-1)


print(compound_interest_3(1000, 0.05, 4, 5))


# 4. Using math.pow
def compound_interest_4(p, r, n, t):
    return p * math.pow((1 + r/n), n*t)


print(compound_interest_4(1000, 0.05, 4, 5))


# 5. Using functools.reduce
def compound_interest_5(p, r, n, t):
    return reduce(lambda acc, _: acc * (1 + r/n), range(n*t), p)


print(compound_interest_5(1000, 0.05, 4, 5))


# 6. Using numpy
def compound_interest_6(p, r, n, t):
    return p * np.power((1 + r/n), n*t)


print(compound_interest_6(1000, 0.05, 4, 5))


# 7. Using Decimal for high precision
def compound_interest_7(p, r, n, t):
    getcontext().prec = 10
    p, r, n = Decimal(p), Decimal(r), Decimal(n)
    return p * (1 + r/n) ** (n*t)


print(compound_interest_7(1000, 0.05, 4, 5))


# 8. Using a function definition instead of lambda
def compound_interest_8(p, r, n, t):
    return p * (1 + r/n) ** (n*t)


print(compound_interest_8(1000, 0.05, 4, 5))


# 9. Using a class
class CompoundInterest:
    def __init__(self, p, r, n, t):
        self.p = p
        self.r = r
        self.n = n
        self.t = t

    def calculate(self):
        return self.p * (1 + self.r/self.n) ** (self.n*self.t)


ci = CompoundInterest(1000, 0.05, 4, 5)
print(ci.calculate())

# 10. Using pandas DataFrame for multiple scenarios


def compound_interest_10(principals, r, n, t):
    df = pd.DataFrame({'Principal': principals})
    df['Amount'] = df['Principal'] * (1 + r/n) ** (n*t)
    return df


print(compound_interest_10([1000, 2000, 3000], 0.05, 4, 5))