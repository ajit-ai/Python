
# Example list with duplicates
nums = [1, 2, 3, 2, 4, 5, 1, 6]

# Find duplicates
duplicates = set()
seen = set()
for num in nums:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print("Duplicates:", list(duplicates))
# Output: Duplicates: [1, 2]

# List with mixed data types
mixed_list = [1, "Hello", 3.14, True, None]

# Print each element with its type
for item in mixed_list:
    print(f"Item: {item}, Type: {type(item)}")
