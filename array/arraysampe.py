import numpy as np

my_list = [1, 2, 3, 4, 5]
your_list = [6, 7, 8, 9, 10]

numpy_array = np.array(my_list)
numpy_array = np.append(numpy_array, your_list)


# Display the properties of the NumPy array
print("Original List: ", my_list)

print("Your List: ", your_list)

print("Combined NumPy Array: ", numpy_array)
print("Minimum Value in Array: ", numpy_array.min())
print("Maximum Value in Array: ", numpy_array.max())
print("Sum of Array Elements: ", numpy_array.sum())

# Display the size, shape, and data type of the NumPy array
print("\nProperties of the NumPy Array:")
print("Array: ", numpy_array)


print("Simple NumPy Array: ", numpy_array)
print("Array Size: ", numpy_array.size)
print("Array Shape: ", numpy_array.shape)
print("Array Data Type: ", numpy_array.dtype)