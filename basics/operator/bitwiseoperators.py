# 1. Bitwise AND of two positive integers
print(5 & 3)  # 1
# 2. Bitwise OR of two positive integers
print(5 | 3)  # 7
# 3. Bitwise XOR of two positive integers
print(5 ^ 3)  # 6
# 4. Bitwise NOT of a positive integer
print(~5)     # -6
# 5. Bitwise NOT of a negative integer
print(~-5)    # 4
# 6. Bitwise AND with zero
print(5 & 0)  # 0
# 7. Bitwise OR with zero
print(5 | 0)  # 5
# 8. Bitwise XOR with zero
print(5 ^ 0)  # 5
# 9. Bitwise AND with itself
print(7 & 7)  # 7
# 10. Bitwise OR with itself
print(7 | 7)  # 7
# 11. Bitwise XOR with itself
print(7 ^ 7)  # 0
# 12. Bitwise AND with all bits set (0xFF)
print(5 & 0xFF)  # 5
# 13. Bitwise OR with all bits set (0xFF)
print(5 | 0xFF)  # 255
# 14. Bitwise XOR with all bits set (0xFF)
print(5 ^ 0xFF)  # 250
# 15. Left shift by 1
print(5 << 1)    # 10
# 16. Left shift by 2
print(5 << 2)    # 20
# 17. Right shift by 1
print(5 >> 1)    # 2
# 18. Right shift by 2
print(5 >> 2)    # 1
# 19. Left shift zero
print(0 << 3)    # 0
# 20. Right shift zero
print(0 >> 3)    # 0
# 21. Left shift negative number
print(-5 << 1)   # -10
# 22. Right shift negative number
print(-5 >> 1)   # -3
# 23. Bitwise AND of negative numbers
print(-5 & -3)
# 24. Bitwise OR of negative numbers
print(-5 | -3)
# 25. Bitwise XOR of negative numbers
print(-5 ^ -3)
# 26. Bitwise AND of positive and negative
print(5 & -3)
# 27. Bitwise OR of positive and negative
print(5 | -3)
# 28. Bitwise XOR of positive and negative
print(5 ^ -3)
# 29. Bitwise AND with 1 (check even/odd)
print(6 & 1)  # 0 (even)
print(7 & 1)  # 1 (odd)
# 30. Bitwise OR with 1
print(6 | 1)  # 7
# 31. Bitwise XOR with 1
print(6 ^ 1)  # 7
# 32. Bitwise AND with mask
print(13 & 0b1100)  # 12
# 33. Bitwise OR with mask
print(13 | 0b0011)  # 15
# 34. Bitwise XOR with mask
print(13 ^ 0b0101)  # 8
# 35. Left shift by 0
print(8 << 0)  # 8
# 36. Right shift by 0
print(8 >> 0)  # 8
# 37. Bitwise NOT of zero
print(~0)      # -1
# 38. Bitwise AND of large numbers
print(1023 & 511)  # 511
# 39. Bitwise OR of large numbers
print(1023 | 511)  # 1023
# 40. Bitwise XOR of large numbers
print(1023 ^ 511)  # 512
# 41. Bitwise AND with negative mask
print(13 & -8)     # 8
# 42. Bitwise OR with negative mask
print(13 | -8)     # -3
# 43. Bitwise XOR with negative mask
print(13 ^ -8)     # -3
# 44. Bitwise AND with 0b1111
print(27 & 0b1111) # 11
# 45. Bitwise OR with 0b1111
print(27 | 0b1111) # 31
# 46. Bitwise XOR with 0b1111
print(27 ^ 0b1111) # 20
# 47. Bitwise AND with 0x0F
print(27 & 0x0F)   # 11
# 48. Bitwise OR with 0x0F
print(27 | 0x0F)   # 31
# 49. Bitwise XOR with 0x0F
print(27 ^ 0x0F)   # 20
# 50. Bitwise AND with 0xF0
print(27 & 0xF0)   # 16
# 51. Bitwise OR with 0xF0
print(27 | 0xF0)   # 255
# 52. Bitwise XOR with 0xF0
print(27 ^ 0xF0)   # 235
# 53. Bitwise AND with 0b101010
print(42 & 0b101010)  # 42
# 54. Bitwise OR with 0b101010
print(21 | 0b101010)  # 63
# 55. Bitwise XOR with 0b101010
print(21 ^ 0b101010)  # 63
# 56. Bitwise AND with 0b010101
print(42 & 0b010101)  # 0
# 57. Bitwise OR with 0b010101
print(42 | 0b010101)  # 63
# 58. Bitwise XOR with 0b010101
print(42 ^ 0b010101)  # 63
# 59. Bitwise AND with 0xAA
print(170 & 0xAA)     # 170
# 60. Bitwise OR with 0xAA
print(85 | 0xAA)      # 255
# 61. Bitwise XOR with 0xAA
print(85 ^ 0xAA)      # 255
# 62. Bitwise AND with 0x55
print(170 & 0x55)     # 0
# 63. Bitwise OR with 0x55
print(170 | 0x55)     # 255
# 64. Bitwise XOR with 0x55
print(170 ^ 0x55)     # 255
# 65. Bitwise AND with 0xFFFF
print(12345 & 0xFFFF) # 12345
# 66. Bitwise OR with 0xFFFF
print(12345 | 0xFFFF) # 65535
# 67. Bitwise XOR with 0xFFFF
print(12345 ^ 0xFFFF) # 53190
# 68. Bitwise AND with 0x0
print(12345 & 0x0)    # 0
# 69. Bitwise OR with 0x0
print(12345 | 0x0)    # 12345
# 70. Bitwise XOR with 0x0
print(12345 ^ 0x0)    # 12345
# 71. Bitwise AND with 0xFFFFFFFF
print(12345 & 0xFFFFFFFF) # 12345
# 72. Bitwise OR with 0xFFFFFFFF
print(12345 | 0xFFFFFFFF) # 4294967295
# 73. Bitwise XOR with 0xFFFFFFFF
print(12345 ^ 0xFFFFFFFF) # 4294954950
# 74. Bitwise AND with 0b1
print(12345 & 0b1)    # 1
# 75. Bitwise OR with 0b1
print(12344 | 0b1)    # 12345
# 76. Bitwise XOR with 0b1
print(12345 ^ 0b1)    # 12344
# 77. Bitwise AND with 0b10
print(12345 & 0b10)   # 0
# 78. Bitwise OR with 0b10
print(12344 | 0b10)   # 12346
# 79. Bitwise XOR with 0b10
print(12345 ^ 0b10)   # 12347
# 80. Bitwise AND with 0b100
print(12345 & 0b100)  # 0
# 81. Bitwise OR with 0b100
print(12344 | 0b100)  # 12348
# 82. Bitwise XOR with 0b100
print(12345 ^ 0b100)  # 12341
# 83. Bitwise AND with 0b1000
print(12345 & 0b1000) # 8
# 84. Bitwise OR with 0b1000
print(12344 | 0b1000) # 12344
# 85. Bitwise XOR with 0b1000
print(12345 ^ 0b1000) # 12353
# 86. Bitwise AND with 0b10000
print(12345 & 0b10000) # 16
# 87. Bitwise OR with 0b10000
print(12344 | 0b10000) # 12360
# 88. Bitwise XOR with 0b10000
print(12345 ^ 0b10000) # 12361
# 89. Bitwise AND with 0b100000
print(12345 & 0b100000) # 32
# 90. Bitwise OR with 0b100000
print(12344 | 0b100000) # 12376
# 91. Bitwise XOR with 0b100000
print(12345 ^ 0b100000) # 12377
# 92. Bitwise AND with 0b1000000
print(12345 & 0b1000000) # 64
# 93. Bitwise OR with 0b1000000
print(12344 | 0b1000000) # 12408
# 94. Bitwise XOR with 0b1000000
print(12345 ^ 0b1000000) # 12409
# 95. Bitwise AND with 0b10000000
print(12345 & 0b10000000) # 128
# 96. Bitwise OR with 0b10000000
print(12344 | 0b10000000) # 12472
# 97. Bitwise XOR with 0b10000000
print(12345 ^ 0b10000000) # 12473
# 98. Bitwise AND with 0b100000000
print(12345 & 0b100000000) # 0
# 99. Bitwise OR with 0b100000000
print(12344 | 0b100000000) # 139528
# 100. Bitwise XOR with 0b100000000
print(12345 ^ 0b100000000) # 139529