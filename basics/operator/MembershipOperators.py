# 1. Integer in list
print(1 in [1, 2, 3])
# 2. Integer not in list
print(4 not in [1, 2, 3])
# 3. String in list
print("a" in ["a", "b", "c"])
# 4. String not in list
print("d" not in ["a", "b", "c"])
# 5. Integer in tuple
print(2 in (1, 2, 3))
# 6. Integer not in tuple
print(4 not in (1, 2, 3))
# 7. String in tuple
print("x" in ("x", "y", "z"))
# 8. String not in tuple
print("w" not in ("x", "y", "z"))
# 9. Integer in set
print(3 in {1, 2, 3})
# 10. Integer not in set
print(5 not in {1, 2, 3})
# 11. String in set
print("cat" in {"cat", "dog"})
# 12. String not in set
print("mouse" not in {"cat", "dog"})
# 13. Integer in dict keys
print(1 in {1: "a", 2: "b"})
# 14. Integer not in dict keys
print(3 not in {1: "a", 2: "b"})
# 15. String in dict keys
print("a" in {"a": 1, "b": 2})
# 16. String not in dict keys
print("c" not in {"a": 1, "b": 2})
# 17. Integer in dict values
print(2 in {"a": 1, "b": 2}.values())
# 18. Integer not in dict values
print(3 not in {"a": 1, "b": 2}.values())
# 19. String in dict values
print("x" in {"a": "x", "b": "y"}.values())
# 20. String not in dict values
print("z" not in {"a": "x", "b": "y"}.values())
# 21. Character in string
print("h" in "hello")
# 22. Character not in string
print("z" not in "hello")
# 23. Substring in string
print("ell" in "hello")
# 24. Substring not in string
print("xyz" not in "hello")
# 25. List in list (checks for element, not sublist)
print([1, 2] in [[1, 2], [3, 4]])
# 26. List not in list
print([5, 6] not in [[1, 2], [3, 4]])
# 27. Tuple in tuple
print((1, 2) in [(1, 2), (3, 4)])
# 28. Tuple not in tuple
print((5, 6) not in [(1, 2), (3, 4)])
# 29. Set in list
print({1, 2} in [{1, 2}, {3, 4}])
# 30. Set not in list
print({5, 6} not in [{1, 2}, {3, 4}])
# 31. Empty string in string
print("" in "abc")
# 32. Empty list in list
print([] in [[], [1]])
# 33. Empty tuple in tuple
print(() in [(), (1,)])
# 34. Empty set in list
print(set() in [set(), {1}])
# 35. 0 in range
print(0 in range(5))
# 36. 5 not in range(5)
print(5 not in range(5))
# 37. 2 in range(1, 10, 2)
print(2 in range(1, 10, 2))
# 38. 3 in range(1, 10, 2)
print(3 in range(1, 10, 2))
# 39. 4 not in range(1, 10, 2)
print(4 not in range(1, 10, 2))
# 40. Character in list of characters
print('a' in ['a', 'b', 'c'])
# 41. Character not in list of characters
print('z' not in ['a', 'b', 'c'])
# 42. String in list of strings
print("apple" in ["apple", "banana"])
# 43. String not in list of strings
print("cherry" not in ["apple", "banana"])
# 44. Integer in string (as character)
print('1' in "123")
# 45. Integer not in string (as character)
print('4' not in "123")
# 46. List in tuple
print([1, 2] in ([1, 2], [3, 4]))
# 47. List not in tuple
print([5, 6] not in ([1, 2], [3, 4]))
# 48. Tuple in list
print((1, 2) in [(1, 2), (3, 4)])
# 49. Tuple not in list
print((5, 6) not in [(1, 2), (3, 4)])
# 50. Dict in list
print({'a': 1} in [{'a': 1}, {'b': 2}])
# 51. Dict not in list
print({'c': 3} not in [{'a': 1}, {'b': 2}])
# 52. Float in list
print(1.1 in [1.1, 2.2])
# 53. Float not in list
print(3.3 not in [1.1, 2.2])
# 54. Float in tuple
print(2.2 in (1.1, 2.2))
# 55. Float not in tuple
print(3.3 not in (1.1, 2.2))
# 56. Float in set
print(1.1 in {1.1, 2.2})
# 57. Float not in set
print(3.3 not in {1.1, 2.2})
# 58. None in list
print(None in [None, 1])
# 59. None not in list
print(None not in [1, 2])
# 60. None in tuple
print(None in (None, 2))
# 61. None not in tuple
print(None not in (1, 2))
# 62. None in set
print(None in {None, 3})
# 63. None not in set
print(None not in {1, 2})
# 64. Boolean in list
print(True in [True, False])
# 65. Boolean not in list
print(False not in [True])
# 66. Boolean in tuple
print(True in (False, True))
# 67. Boolean not in tuple
print(False not in (True,))
# 68. Boolean in set
print(True in {False, True})
# 69. Boolean not in set
print(False not in {True})
# 70. Object in list
class A: pass
a = A()
b = A()
print(a in [a, b])
# 71. Object not in list
print(A() not in [a, b])
# 72. Object in tuple
print(a in (a, b))
# 73. Object not in tuple
print(A() not in (a, b))
# 74. Object in set
print(a in {a, b})
# 75. Object not in set
print(A() not in {a, b})
# 76. String in bytes (not allowed, will be False)
print("a" in b"abc".decode())
# 77. Byte in bytes
print(b"a" in b"abc")
# 78. Byte not in bytes
print(b"d" not in b"abc")
# 79. String in frozenset
print("x" in frozenset(["x", "y"]))
# 80. String not in frozenset
print("z" not in frozenset(["x", "y"]))
# 81. Integer in frozenset
print(1 in frozenset([1, 2]))
# 82. Integer not in frozenset
print(3 not in frozenset([1, 2]))
# 83. Membership in generator
print(2 in (i for i in range(5)))
# 84. Membership not in generator
print(6 not in (i for i in range(5)))
# 85. Membership in map object
print(4 in map(lambda x: x * 2, range(3)))
# 86. Membership not in map object
print(7 not in map(lambda x: x * 2, range(3)))
# 87. Membership in filter object
print(2 in filter(lambda x: x % 2 == 0, range(5)))
# 88. Membership not in filter object
print(5 not in filter(lambda x: x % 2 == 0, range(5)))
# 89. Membership in string with whitespace
print(" " in "hello world")
# 90. Membership not in string with whitespace
print("z" not in "hello world")
# 91. Membership in nested list
print(2 in [1, [2, 3]])
# 92. Membership in nested list (as sublist)
print([2, 3] in [1, [2, 3]])
# 93. Membership in nested tuple
print(2 in (1, (2, 3)))
# 94. Membership in nested tuple (as subtuple)
print((2, 3) in (1, (2, 3)))
# 95. Membership in dict with tuple keys
print((1, 2) in {(1, 2): "a", (3, 4): "b"})
# 96. Membership not in dict with tuple keys
print((5, 6) not in {(1, 2): "a", (3, 4): "b"})
# 97. Membership in dict with int keys
print(1 in {1: "a", 2: "b"})
# 98. Membership not in dict with int keys
print(3 not in {1: "a", 2: "b"})
# 99. Membership in dict with string keys
print("a" in {"a": 1, "b": 2})
# 100. Membership not in dict with string keys
print("c" not in {"a": 1, "b": 2})