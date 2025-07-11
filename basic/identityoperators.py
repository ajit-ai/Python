import sys
import math


# 1. Integers, same value, different objects
a = 1000
b = 1000
print(a is b)  # False (for large ints, different objects)
# 2. Integers, small value, same object (CPython optimization)
a = 10
b = 10
print(a is b)  # True
# 3. Floats
a = 1.1
b = 1.1
print(a is b)  # False
# 4. Strings, same literal
a = "hello"
b = "hello"
print(a is b)  # True
# 5. Strings, constructed
a = "".join(["he", "llo"])
b = "hello"
print(a is b)  # May be False
# 6. Lists, same content, different objects
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # False
# 7. Lists, same object
a = [1, 2, 3]
b = a
print(a is b)  # True
# 8. Tuples, same content, different objects
a = (1, 2)
b = (1, 2)
print(a is b)  # May be True or False
# 9. Tuples, same object
a = (1, 2)
b = a
print(a is b)  # True
# 10. Sets, same content, different objects
a = {1, 2}
b = {1, 2}
print(a is b)  # False
# 11. Sets, same object
a = {1, 2}
b = a
print(a is b)  # True
# 12. Dicts, same content, different objects
a = {'x': 1}
b = {'x': 1}
print(a is b)  # False
# 13. Dicts, same object
a = {'x': 1}
b = a
print(a is b)  # True
# 14. None comparison
a = None
b = None
print(a is b)  # True
# 15. Custom objects, different instances
class A: pass


a = A()
b = A()
print(a is b)  # False
# 16. Custom objects, same instance
a = A()
b = a
print(a is b)  # True
# 17. is not with integers
a = 5
b = 6
print(a is not b)  # True
# 18. is not with lists
a = [1]
b = [1]
print(a is not b)  # True
# 19. is not with same list
a = [1]
b = a
print(a is not b)  # False
# 20. is with bools
a = True
b = True
print(a is b)  # True
# 21. is not with bools
a = True
b = False
print(a is not b)  # True
# 22. is with empty tuple
a = ()
b = ()
print(a is b)  # True
# 23. is with empty list
a = []
b = []
print(a is b)  # False
# 24. is with empty dict
a = {}
b = {}
print(a is b)  # False
# 25. is with empty set
a = set()
b = set()
print(a is b)  # False
# 26. is with frozenset
a = frozenset()
b = frozenset()
print(a is b)  # False
# 27. is with bytes
a = b"bytes"
b = b"bytes"
print(a is b)  # True
# 28. is with bytearray
a = bytearray(b"bytes")
b = bytearray(b"bytes")
print(a is b)  # False
# 29. is with memoryview
a = memoryview(b"bytes")
b = memoryview(b"bytes")
print(a is b)  # False
# 30. is with range
a = range(5)
b = range(5)
print(a is b)  # False
# 31. is with same range object
a = range(5)
b = a
print(a is b)  # True
# 32. is with function objects
def f(): pass
def g(): pass


print(f is g)  # False
# 33. is with same function
def f(): pass
a = f
b = f
print(a is b)  # True
# 34. is with lambda
a = lambda x: x
b = lambda x: x
print(a is b)  # False
# 35. is with same lambda
a = lambda x: x
b = a
print(a is b)  # True
# 36. is with class objects
class B: pass
a = B
b = B
print(a is b)  # True
# 37. is with different class objects
class C: pass
class D: pass
print(C is D)  # False
# 38. is with modules

a = math
b = math
print(a is b)  # True
# 39. is with different modules

print(math is sys)  # False
# 40. is with built-in types
a = int
b = int
print(a is b)  # True
# 41. is with different built-in types
a = int
b = float
print(a is b)  # False
# 42. is with True and 1
#print(True is 1)  # False
# 43. is with False and 0
#print(False is 0)  # False
# 44. is not with None
a = None
print(a is not None)  # False
# 45. is with object()
a = object()
b = object()
print(a is b)  # False
# 46. is with same object()
a = object()
b = a
print(a is b)  # True
# 47. is with id()
a = [1]
b = a
print(id(a) == id(b))  # True
# 48. is not with id()
a = [1]
b = [1]
print(id(a) != id(b))  # True
# 49. is with nested lists
a = [[1]]
b = [[1]]
print(a is b)  # False
# 50. is with same nested list
a = [[1]]
b = a
print(a is b)  # True
# 51. is with generator
a = (i for i in range(3))
b = (i for i in range(3))
print(a is b)  # False
# 52. is with same generator
a = (i for i in range(3))
b = a
print(a is b)  # True
# 53. is with bool() objects
a = bool(1)
b = bool(1)
print(a is b)  # True
# 54. is with int() objects
a = int(5)
b = int(5)
print(a is b)  # True (for small ints)
# 55. is with float() objects
a = float(5)
b = float(5)
print(a is b)  # False
# 56. is with str() objects
a = str("abc")
b = str("abc")
print(a is b)  # True
# 57. is with list() objects
a = list([1,2])
b = list([1,2])
print(a is b)  # False
# 58. is with tuple() objects
a = tuple((1,2))
b = tuple((1,2))
print(a is b)  # True or False
# 59. is with set() objects
a = set([1,2])
b = set([1,2])
print(a is b)  # False
# 60. is with frozenset() objects
a = frozenset([1,2])
b = frozenset([1,2])
print(a is b)  # False
# 61. is with bytes() objects
a = bytes([1,2])
b = bytes([1,2])
print(a is b)  # False
# 62. is with bytearray() objects
a = bytearray([1,2])
b = bytearray([1,2])
print(a is b)  # False
# 63. is with memoryview() objects
a = memoryview(bytes([1,2]))
b = memoryview(bytes([1,2]))
print(a is b)  # False
# 64. is with bool and int
print(True is int(1))  # False
# 65. is with False and int(0)
print(False is int(0))  # False
# 66. is with float and int
print(float(1) is int(1))  # False
# 67. is with string interning
a = "short"
b = "short"
print(a is b)  # True
# 68. is with long strings
a = "a" * 1000
b = "a" * 1000
print(a is b)  # May be False
# 69. is with bytes interning
a = b"short"
b = b"short"
print(a is b)  # True
# 70. is with empty string
a = ""
b = ""
print(a is b)  # True
# 71. is with empty bytes
a = b""
b = b""
print(a is b)  # True
# 72. is with empty frozenset
a = frozenset()
b = frozenset()
print(a is b)  # False
# 73. is with empty range
a = range(0)
b = range(0)
print(a is b)  # False
# 74. is with same range object
a = range(0)
b = a
print(a is b)  # True
# 75. is with bool and bool
a = bool(True)
b = bool(True)
print(a is b)  # True
# 76. is with int and bool
a = int(True)
b = bool(True)
print(a is b)  # False
# 77. is with float and bool
a = float(True)
b = bool(True)
print(a is b)  # False
# 78. is with int and float
a = int(1)
b = float(1)
print(a is b)  # False
# 79. is with int and str
a = int(1)
b = str(1)
print(a is b)  # False
# 80. is with float and str
a = float(1)
b = str(1)
print(a is b)  # False
# 81. is with list and tuple
a = [1,2]
b = (1,2)
print(a is b)  # False
# 82. is with set and frozenset
a = set([1,2])
b = frozenset([1,2])
print(a is b)  # False
# 83. is with dict and set
a = {'a':1}
b = set(['a'])
print(a is b)  # False
# 84. is with list and set
a = [1,2]
b = set([1,2])
print(a is b)  # False
# 85. is with tuple and frozenset
a = (1,2)
b = frozenset([1,2])
print(a is b)  # False
# 86. is with int and None
a = 1
b = None
print(a is b)  # False
# 87. is with float and None
a = 1.0
b = None
print(a is b)  # False
# 88. is with str and None
a = "abc"
b = None
print(a is b)  # False
# 89. is with list and None
a = []
b = None
print(a is b)  # False
# 90. is with dict and None
a = {}
b = None
print(a is b)  # False
# 91. is with set and None
a = set()
b = None
print(a is b)  # False
# 92. is with tuple and None
a = ()
b = None
print(a is b)  # False
# 93. is with frozenset and None
a = frozenset()
b = None
print(a is b)  # False
# 94. is with bytes and None
a = b""
b = None
print(a is b)  # False
# 95. is with bytearray and None
a = bytearray()
b = None
print(a is b)  # False
# 96. is with memoryview and None
a = memoryview(b"")
b = None
print(a is b)  # False
# 97. is with function and None
def foo(): pass
a = foo
b = None
print(a is b)  # False
# 98. is with class and None
class E: pass
a = E
b = None
print(a is b)  # False
# 99. is with module and None
a = math
b = None
print(a is b)  # False
# 100. is with object and None
a = object()
b = None
print(a is b)  # False

L = ['red', 'green', 'blue']

# in
print('red' in L)           # True

# not in
print('yellow' not in L)    # True