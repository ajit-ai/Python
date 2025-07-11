# Numbers
print(1 == 1)
print(1 != 2)
print(3 > 2)
print(2 < 3)
print(3 >= 3)
print(2 <= 3)
print(-1 < 0)
print(0 == 0)
print(100 > 99)
print(50 <= 50)

# Floats
print(1.1 == 1.1)
print(1.1 != 2.2)
print(3.5 > 2.5)
print(2.5 < 3.5)
print(3.5 >= 3.5)
print(2.5 <= 3.5)
print(-1.1 < 0.0)
print(0.0 == 0.0)
print(100.1 > 99.9)
print(50.5 <= 50.5)

# Strings
print("a" == "a")
print("a" != "b")
print("b" > "a")
print("a" < "b")
print("abc" >= "abc")
print("abc" <= "abd")
print("A" < "a")
print("abc" == "abc")
print("abc" != "ABC")
print("abc" > "ab")

# Lists
print([1, 2] == [1, 2])
print([1, 2] != [2, 1])
print([1, 2, 3] > [1, 2])
print([1, 2] < [1, 2, 3])
print([1, 2, 3] >= [1, 2, 3])
print([1, 2] <= [1, 2, 3])
print([] < [1])
print([1] == [1])
print([1, 2] != [1, 2, 3])
print([1, 2, 3] > [1, 2, 2])

# Tuples
print((1, 2) == (1, 2))
print((1, 2) != (2, 1))
print((1, 2, 3) > (1, 2))
print((1, 2) < (1, 2, 3))
print((1, 2, 3) >= (1, 2, 3))
print((1, 2) <= (1, 2, 3))
print( () < (1,) )
print((1,) == (1,))
print((1, 2) != (1, 2, 3))
print((1, 2, 3) > (1, 2, 2))

# Sets (only == and !=)
print({1, 2} == {2, 1})
print({1, 2} != {1, 2, 3})
print(set() == set())
print({1, 2, 3} != {3, 2, 1, 0})
print({1} == {1})
print({1, 2, 3} != {1, 2})
print({1, 2, 3} == {3, 2, 1})
print({1, 2} != {2, 3})
print({1, 2, 3} == {1, 2, 3})
print({1, 2, 3} != {1, 2, 4})

# Dictionaries (only == and !=)
print({'a': 1, 'b': 2} == {'b': 2, 'a': 1})
print({'a': 1, 'b': 2} != {'a': 1, 'b': 3})
print({} == {})
print({'a': 1} != {'a': 2})
print({'a': 1, 'b': 2} == {'a': 1, 'b': 2})
print({'a': 1, 'b': 2} != {'a': 1})
print({'a': 1, 'b': 2} == {'b': 2, 'a': 1})
print({'a': 1} != {'b': 1})
print({'a': 1, 'b': 2} == {'a': 1, 'b': 2})
print({'a': 1, 'b': 2} != {'a': 1, 'b': 3})

# Mixed types
print(1 == 1.0)
print(1 != 1.1)
print(1 < 1.1)
print(1.1 > 1)
print("1" == 1)
print("1" != 1)
print([1] == (1,))
print([1] != (1,))
print({1} == [1])
print({1} != [1])

# Custom objects
class A:
    def __init__(self, v): self.v = v
    def __eq__(self, other): return self.v == other.v
    def __ne__(self, other): return self.v != other.v
    def __lt__(self, other): return self.v < other.v
    def __le__(self, other): return self.v <= other.v
    def __gt__(self, other): return self.v > other.v
    def __ge__(self, other): return self.v >= other.v

a1 = A(5)
a2 = A(10)
print(a1 == a2)
print(a1 != a2)
print(a1 < a2)
print(a1 > a2)
print(a1 <= a2)
print(a1 >= a2)
print(a1 == A(5))
print(a2 != A(5))
print(a1 < A(6))
print(a2 > A(9))

# Boolean comparisons
print(True == 1)
print(False == 0)
print(True != 0)
print(False != 1)
print(True > False)
print(False < True)
print(True >= False)
print(False <= True)
print(True == True)
print(False == False)