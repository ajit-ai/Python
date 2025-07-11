import math
from functools import reduce
import operator


# 1. Addition of integers
print(2 + 3)
# 2. Addition of floats
print(2.5 + 3.1)
# 3. Addition of negative numbers
print(-2 + 3)
# 4. Addition of zero
print(0 + 5)
# 5. Addition of large numbers
print(1000000 + 999999)
# 6. Subtraction of integers
print(5 - 2)
# 7. Subtraction of floats
print(5.5 - 2.2)
# 8. Subtraction resulting in negative
print(2 - 5)
# 9. Subtraction with zero
print(5 - 0)
# 10. Multiplication of integers
print(4 * 3)
# 11. Multiplication of floats
print(2.5 * 4.0)
# 12. Multiplication with zero
print(5 * 0)
# 13. Multiplication with negative
print(-3 * 4)
# 14. Multiplication of large numbers
print(1000 * 1000)
# 15. Division of integers
print(10 / 2)
# 16. Division of floats
print(7.5 / 2.5)
# 17. Division resulting in float
print(7 / 2)
# 18. Division by negative
print(10 / -2)
# 19. Division by 1
print(10 / 1)
# 20. Floor division of integers
print(7 // 2)
# 21. Floor division of floats
print(7.5 // 2.5)
# 22. Floor division with negative
print(-7 // 2)
# 23. Floor division by 1
print(7 // 1)
# 24. Modulus of integers
print(7 % 2)
# 25. Modulus of floats
print(7.5 % 2.5)
# 26. Modulus with negative
print(-7 % 2)
# 27. Modulus by 1
print(7 % 1)
# 28. Exponentiation (power)
print(2 ** 3)
# 29. Exponentiation with negative exponent
print(2 ** -2)
# 30. Exponentiation with zero exponent
print(5 ** 0)
# 31. Exponentiation with float base
print(2.5 ** 2)
# 32. Exponentiation with float exponent
print(9 ** 0.5)
# 33. Addition assignment
x = 5
x += 3
print(x)
# 34. Subtraction assignment
x -= 2
print(x)
# 35. Multiplication assignment
x *= 4
print(x)
# 36. Division assignment
x /= 2
print(x)
# 37. Floor division assignment
x //= 3
print(x)
# 38. Modulus assignment
x %= 2
print(x)
# 39. Exponentiation assignment
x **= 4
print(x)
# 40. Chained addition
print(1 + 2 + 3 + 4)
# 41. Chained subtraction
print(10 - 2 - 3)
# 42. Chained multiplication
print(2 * 3 * 4)
# 43. Chained division
print(100 / 2 / 5)
# 44. Chained floor division
print(100 // 3 // 2)
# 45. Chained modulus
print(100 % 7 % 3)
# 46. Chained exponentiation
print(2 ** 3 ** 2)
# 47. Mixed operators
print(2 + 3 * 4)
# 48. Parentheses to change precedence
print((2 + 3) * 4)
# 49. Negative numbers in expressions
print(-2 + 3 * -4)
# 50. Absolute value
print(abs(-10 + 5))
# 51. Multiplying lists (repetition)
print([1, 2] * 3)
# 52. Adding lists (concatenation)
print([1, 2] + [3, 4])
# 53. Multiplying tuples (repetition)
print((1, 2) * 2)
# 54. Adding tuples (concatenation)
print((1, 2) + (3, 4))
# 55. Multiplying strings
print("hi" * 3)
# 56. Adding strings
print("hi" + " there")
# 57. Using pow()
print(pow(2, 5))
# 58. Using divmod()
print(divmod(17, 3))


# 59. Using math.fsum()
print(math.fsum([0.1, 0.2, 0.3]))
# 60. Using math.prod()
print(math.prod([2, 3, 4]))
# 61. Using math.remainder()
print(math.remainder(10, 3))
# 62. Using math.isclose()
print(math.isclose(0.1 + 0.2, 0.3))
# 63. Using round()
print(round(3.14159, 2))
# 64. Using ceil()
print(math.ceil(2.3))
# 65. Using floor()
print(math.floor(2.7))
# 66. Using trunc()
print(math.trunc(2.9))
# 67. Using copysign()
print(math.copysign(3, -1))
# 68. Using hypot()
print(math.hypot(3, 4))
# 69. Using sqrt()
print(math.sqrt(16))
# 70. Using log()
print(math.log(100, 10))
# 71. Using exp()
print(math.exp(2))
# 72. Using factorial()
print(math.factorial(5))
# 73. Using sum() with generator
print(sum(i for i in range(5)))
# 74. Using reduce() for sum
print(reduce(lambda x, y: x + y, [1, 2, 3, 4]))
# 75. Using reduce() for product
print(reduce(lambda x, y: x * y, [1, 2, 3, 4]))
# 76. Using operator.add
print(operator.add(2, 3))
# 77. Using operator.sub
print(operator.sub(5, 2))
# 78. Using operator.mul
print(operator.mul(3, 4))
# 79. Using operator.truediv
print(operator.truediv(10, 4))
# 80. Using operator.floordiv
print(operator.floordiv(10, 4))
# 81. Using operator.mod
print(operator.mod(10, 3))
# 82. Using operator.pow
print(operator.pow(2, 4))
# 83. Using operator.neg
print(operator.neg(5))
# 84. Using operator.pos
print(operator.pos(-5))
# 85. Using operator.abs
print(operator.abs(-7))
# 86. Using operator.iadd
x = 5
x = operator.iadd(x, 3)
print(x)
# 87. Using operator.isub
x = operator.isub(x, 2)
print(x)
# 88. Using operator.imul
x = operator.imul(x, 4)
print(x)
# 89. Using operator.itruediv
x = operator.itruediv(x, 2)
print(x)
# 90. Using operator.ifloordiv
x = operator.ifloordiv(x, 3)
print(x)
# 91. Using operator.imod
x = operator.imod(x, 2)
print(x)
# 92. Using operator.ipow
x = operator.ipow(x, 4)
print(x)
# 93. Using sum() with start value
print(sum([1, 2, 3], 10))
# 94. Using math.comb()
print(math.comb(5, 2))
# 95. Using math.perm()
print(math.perm(5, 2))
# 96. Using math.gcd()
print(math.gcd(48, 18))
# 97. Using math.lcm()
print(math.lcm(12, 15))
# 98. Using math.dist()
print(math.dist([0, 0], [3, 4]))
# 99. Using math.isqrt()
print(math.isqrt(17))
# 100. Using math.nextafter()
print(math.nextafter(1, 2))