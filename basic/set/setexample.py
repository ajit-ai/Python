s = {10, 50, 20}
print(s)
print(type(s))

# typecasting list to set
s = set(["a", "b", "c"])
print(s)

# Adding element to the set
s.add("d")
print(s)

# Removing element from the set
s.remove("b")
print(s)

# Discarding an element from the set
s.discard("c")
print(s)

# Popping an element from the set
popped_element = s.pop()
print(popped_element)
print(s)

# Checking if an element exists in the set
print("a" in s)

# Finding the length of the set
print(len(s))

# Creating a set with mixed data types
s = {1, "hello", 3.14, (1, 2)}
print(s)


# Clearing the set
s.clear()
print(s)


# a set cannot have duplicate values
s = {"India", "Delhi", "Rajasthan", "Mumbai"}
print(s)

# Adding a duplicate value
s.add("Delhi")

# Same as {"a", "b","c"}
s = set(["a", "b", "c"])

print("Normal Set")
print(s)

# A frozen set
fs = frozenset(["e", "f", "g"])

print("\nFrozen Set")
print(fs)

