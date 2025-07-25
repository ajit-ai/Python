import array

# Create an array of integers
arr = array.array('i', [1, 2, 3, 4, 5, 9])

# Create an array of floats
arr_float = array.array('f', [1.1, 2.2, 3.3])

# Print the float array
print(arr_float)  # Output: array('f', [1.100000023841858, 2.200000047683716, 3.299999952316284])

# Create an array of characters
arr_char = array.array('u', 'hello')

# Print the character array
print(arr_char)  # Output: array('u', 'hello')

# Print the float array
print(arr_float)  # Output: array('f', [1.100000023841858, 2.200000047683716, 3.299999952316284])

# Print the original array
print(arr)  # Output: array('i', [1, 2, 3, 4, 5, 9])

# Access elements
print(arr[0])  # Output: 1

# Append an element
arr.append(6)

# Count a set of elements
print(arr.count(1))  # Output: 1

# Remove an element
arr.remove(2)

# Print the modified array
print(arr)  # Output: array('i', [1, 3, 4, 5, 9, 6])

# Convert to list
arr_list = arr.tolist()
print(arr_list)  # Output: [1, 3, 4, 5, 9, 6]

# Convert to bytes
arr_bytes = arr.tobytes()
print(arr_bytes)

# Print the byte representation
print(arr_bytes)  # Output: b'\x01\x00\x00\x00\x

# Arrange the array in ascending order
arr = array.array('i', sorted(arr))

print(arr)  # Output: array('i', [1, 3, 4, 5, 6, 9])

# Iterate through the array

for num in arr:
    print(num)