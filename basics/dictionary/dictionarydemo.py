# Creating a Dictionary
d = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("Creating Dictionary: ")
print(d)

# accessing a element using key 
print("Accessing a element using key:") 
print(d['Name']) 

# accessing a element using get() 
# method 
print("Accessing a element using get:") 
print(d.get(1)) 

# creation using Dictionary comprehension
myDict = {x: x**2 for x in [1,2,3,4,5]}
print(myDict)


# Dictionaries are a key-value object in Python.
# Like sets, you create them using { and }, but unlike sets, they must be
# created as key-value pairs using the : symbol.
# The values used can be any object.
my_dictionary = {'banana': '$10.00', 'cheese': True}

# Access items like with lists, except keys are usually strings.
my_dictionary['banana']  # returns the string '$10.00'
my_dictionary['cheese']  # returns True

# If accessing a key that doesn't exist using [ ], Python raises a KeyError.
# e.g. my_dictionary['optimus'] will raise a KeyError.

# Adding new items.
my_dictionary['optimus'] = 'Truck'

# Changing existing items.
my_dictionary['cheese'] = False

# Get all the keys. (used for looping/iterating later on)
my_dictionary.keys()

# Get all the values.
my_dictionary.values()

# Get all the items (key-value pairs)
my_dictionary.items()

# See help(dict) for other methods.