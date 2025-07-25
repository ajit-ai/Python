type(23)

type(3.14)

type(True)

type(-12.4)

type("hello")

type("a")


# Convert from float to int
number = int(3.14)
type(number)

# Convert from int to float
number = float(3)
type(number)

# Convert from string to int
number = int("1234")
type(number)

# Convert from string to float
number = float("12.345")
type(number)

# Convert from bool to string
value = str(True)
type(value)

# Convert from string to bool
value = bool('False')

# Convert from int to bool
bool(0)
bool(1)
bool(5)
bool(-2)

# Convert from float to bool
bool(0.0)
bool(0.1)
bool(-0.0)

# Weird behaviour:
1234 + True  # gives 1235 because "True" is 1 internally.
1234 + 5*True  # gives 1239
1234 - True  # gives 1233
1234 / False  # gives ZeroDivisionError
