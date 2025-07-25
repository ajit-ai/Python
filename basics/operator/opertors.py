# from functools import reduce

x = 5
y = 10
z = [1, 2, 3, 4, 5]
a = [5, 10, 15]
b = [1, 2, 3]
s = "ajit"
t = "kumar"
d = {'a': 1, 'b': 2}
f = 3.5
g = 2.0


# 1. Addition
print(x + y)
# 2. Subtraction
print(x - y)
# 3. Multiplication
print(x * y)
# 4. Division
print(x / y)
# 5. Floor division
print(x // y)
# 6. Modulus
print(x % y)
# 7. Exponentiation
print(x ** 2)
# 8. Negative
print(-x)
# 9. Positive
print(+x)
# 10. Absolute
print(abs(-x))
# 11. In-place addition
x += 1
print(x)
# 12. In-place subtraction
x -= 1
print(x)
# 13. In-place multiplication
x *= 2
print(x)
# 14. In-place division
x /= 2
print(x)
# 15. In-place floor division
x //= 2
print(x)
# 16. In-place modulus
x %= 2
print(x)
# 17. In-place exponentiation
x **= 3
print(x)
# 18. Bitwise AND
print(y & 3)
# 19. Bitwise OR
print(y | 3)
# 20. Bitwise XOR
print(y ^ 3)
# 21. Bitwise NOT
print(~y)
# 22. Left shift
print(y << 2)
# 23. Right shift
print(y >> 2)
# 24. In-place bitwise AND
y &= 7
print(y)
# 25. In-place bitwise OR
y |= 2
print(y)
# 26. In-place bitwise XOR
y ^= 1
print(y)
# 27. In-place left shift
y <<= 1
print(y)
# 28. In-place right shift
y >>= 1
print(y)
# 29. Equal to
print(x == y)
# 30. Not equal to
print(x != y)
# 31. Greater than
print(x > y)
# 32. Less than
print(x < y)
# 33. Greater than or equal to
print(x >= y)
# 34. Less than or equal to
print(x <= y)
# 35. Logical AND
print(x and y)
# 36. Logical OR
print(x or y)
# 37. Logical NOT
print(not x)
# 38. Identity is
print(x is y)
# 39. Identity is not
print(x is not y)
# 40. Membership in (list)
print(5 in z)
# 41. Membership not in (list)
print(6 not in z)
# 42. Membership in (string)
print('h' in s)
# 43. Membership not in (string)
print('z' not in s)
# 44. Membership in (dict keys)
print('a' in d)
# 45. Membership in (dict values)
print(1 in d.values())
# 46. Chained comparison
print(1 < x < 10)
# 47. Ternary operator
print(x if x > y else y)
# 48. Tuple unpacking
a1, a2, a3 = a
print(a1, a2, a3)
# 49. List concatenation
print(a + b)
# 50. List repetition
print(b * 2)
# 51. String concatenation
print(s + t)
# 52. String repetition
print(s * 3)
# 53. String slicing
print(s[1:4])
# 54. List slicing
print(z[1:3])
# 55. List comprehension with operator
print([i * 2 for i in z])
# 56. All operator
print(all([True, False, True]))
# 57. Any operator
print(any([False, False, True]))
# 58. Max operator
print(max(z))
# 59. Min operator
print(min(z))
# 60. Sum operator
print(sum(z))
# 61. Map with operator
print(list(map(lambda x: x + 1, z)))
# 62. Filter with operator
# print(reduce(lambda x, y: x + y, z))
# print(reduce(lambda x, y: x + y, z))


# 64. Operator overloading (custom class)
class Point:
    def __init__(self, x): self.x = x
    def __add__(self, other): return Point(self.x + other.x)
    def __str__(self): return str(self.x)


p1 = Point(2)
p2 = Point(3)
print(p1 + p2)
# 65. Logical short-circuit
print(False and print("won't print"))
print(True or print("won't print"))
# 66. is operator with None
print(x is None)
# 67. not operator with None
print(not None)
# 68. List in-place addition
z += [6]
print(z)
# 69. List in-place multiplication
b *= 2
print(b)
# 70. String in-place concatenation
s += "!"
print(s)
# 71. String in-place repetition
t *= 2
print(t)
# 72. Dict key assignment
d['c'] = 3
print(d)
# 73. Dict value update
d['a'] += 1
print(d)
# 74. Dict pop
d.pop('b')
print(d)
# 75. Dict get
print(d.get('c'))
# 76. Set union
print(set(a) | set(b))
# 77. Set intersection
print(set(a) & set(b))
# 78. Set difference
print(set(a) - set(b))
# 79. Set symmetric difference
print(set(a) ^ set(b))
# 80. Set in-place union
s1 = set([1, 2])
s1 |= set([2, 3])
print(s1)
# 81. Set in-place intersection
s1 &= set([2])
print(s1)
# 82. Set in-place difference
s1 -= set([2])
print(s1)
# 83. Set in-place symmetric difference
s1 ^= set([1, 3])
print(s1)
# 84. List index assignment
z[0] = 100
print(z)
# 85. List append
z.append(200)
print(z)
# 86. List pop
z.pop()
print(z)
# 87. List remove
z.remove(100)
print(z)
# 88. List insert
z.insert(0, 50)
print(z)
# 89. List clear
z.clear()
print(z)
# 90. List extend
z.extend([1, 2, 3])
print(z)
# 91. List reverse
z.reverse()
print(z)
# 92. List sort
z.sort()
print(z)
# 93. List count
print(z.count(2))
# 94. List copy
z2 = z.copy()
print(z2)
# 95. Tuple creation
tup = (1, 2, 3)
print(tup)
# 96. Tuple unpacking
a, b, c = tup
print(a, b, c)
# 97. Tuple concatenation
print(tup + (4, 5))
# 98. Tuple repetition
print(tup * 2)
# 99. Tuple slicing
print(tup[1:])
# 100. Tuple membership
print(2 in tup)