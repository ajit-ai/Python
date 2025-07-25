# Unlike arrays in most other languages, Python lists can store data of any type.

# Create a list with [ and ]
my_list = [1, 2, "this is a list", 4.56, True]

# Lists have the following methods:
# append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort

# Accessing an item in a list using index, same as tuples.
my_list[2]  # displays "this is a list"

# Appending an item (only 1 item can be appended at a time).
my_list.append(123)  # Appends 123 on to the end of the list.

# Insert an item at a particular index.
my_list.insert(0, 'hello')  # inserts 'hello' at the beginning (index 0) of list.
my_list.insert(2, 'blahblah')  # inserts 'blahblah' at index 2.

# "pop" an item from a list, which accesses an item and removes it.
# defaults to end of list if no index is given as an argument.
my_list.pop()  # removes last item from the list
my_list.pop(2)  # gets and removes item at index 2

# "remove" differs from pop. pop uses an index. remove searches for the value and removes the first instance of it.
my_list.remove("hello")  # searches for "hello" and removes 1st instance if found.

# Reverse the list (changes the actual list "in place").
my_list.reverse()

# Sort the list in ascending order. Advanced sorting can control how it's sorted.
# my_list.sort()

# Copy the list. Returns a "shallow copy". Read more about what this means later.
my_list2 = my_list.copy()

# Count the number of occurrences of a value.
my_list.count("hello")

# Extend the list, aka add multiple items at a time.
my_list.extend(["x", 102, False])

# Return the first index of a value. (without changing the list)
# my_list.index("hello")  # You can also tell it where to start/stop searching.

# Clear the list.
my_list.clear()