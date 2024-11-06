# data_types.py
# This file demonstrates Python's basic data types and structures with examples.

# =====================
# 1. Basic Data Types
# =====================

# Integer - whole numbers, positive or negative
int_var = 10
print(f"Integer: {int_var}")  # Output: 10

# Float - numbers with a decimal point
float_var = 10.5
print(f"Float: {float_var}")  # Output: 10.5

# String - sequence of characters, defined with single or double quotes
str_var = "Hello, World!"
print(f"String: {str_var}")  # Output: Hello, World!

# Boolean - represents True or False
bool_var = True
print(f"Boolean: {bool_var}")  # Output: True

# Complex - numbers with real and imaginary parts, represented as `a + bj`
complex_var = 3 + 5j
print(f"Complex Number: {complex_var}")  # Output: (3+5j)

# =====================
# 2. Basic Data Structures
# =====================

# List - an ordered, mutable sequence of elements, allowing duplicates
list_var = [1, 2, 3, "apple", 4.5]
print(f"List: {list_var}")  # Output: [1, 2, 3, 'apple', 4.5]
print(f"First Element in List: {list_var[0]}")  # Access first element

# Tuple - an ordered, immutable sequence of elements, allowing duplicates
tuple_var = (1, 2, 3, "banana")
print(f"Tuple: {tuple_var}")  # Output: (1, 2, 3, 'banana')
print(f"Second Element in Tuple: {tuple_var[1]}")  # Access second element

# Dictionary - stores key-value pairs, keys must be unique
dict_var = {"name": "Alice", "age": 25}
print(f"Dictionary: {dict_var}")  # Output: {'name': 'Alice', 'age': 25}
print(f"Value by Key 'name': {dict_var['name']}")  # Access value by key

# Set - an unordered collection of unique elements, no duplicates allowed
set_var = {1, 2, 3, 3, 4}  # Duplicate 3 will be removed
print(f"Set: {set_var}")  # Output: {1, 2, 3, 4}

# =====================
# 3. Special Data Types
# =====================

# NoneType - represents the absence of a value, used for null values
none_var = None
print(f"NoneType: {none_var}")  # Output: None

# Bytes - immutable sequence of bytes, often used for binary data
bytes_var = b"hello"
print(f"Bytes: {bytes_var}")  # Output: b'hello'

# Bytearray - mutable sequence of bytes
bytearray_var = bytearray(5)
print(f"Bytearray: {bytearray_var}")  # Output: bytearray(b'\x00\x00\x00\x00\x00')

# =====================
# 4. Type Conversion
# =====================

# Convert integer to float
int_to_float = float(int_var)
print(f"Integer to Float: {int_to_float}")  # Output: 10.0

# Convert float to integer (truncates decimal part)
float_to_int = int(float_var)
print(f"Float to Integer: {float_to_int}")  # Output: 10

# Convert string to integer
str_to_int = int("42")
print(f"String to Integer: {str_to_int}")  # Output: 42

# Convert list to tuple
list_to_tuple = tuple(list_var)
print(f"List to Tuple: {list_to_tuple}")

# Convert tuple to list
tuple_to_list = list(tuple_var)
print(f"Tuple to List: {tuple_to_list}")

# Convert set to list (order is not preserved)
set_to_list = list(set_var)
print(f"Set to List: {set_to_list}")

# =====================
# 5. Useful Functions
# =====================

# len() - returns the number of elements in a data structure
print(f"Length of List: {len(list_var)}")  # Output: 5

# type() - returns the data type of a variable
print(f"Type of int_var: {type(int_var)}")  # Output: <class 'int'>

# max() and min() - return the maximum and minimum values in a collection
print(f"Max in List: {max(list_var[:3])}")  # Output: 3
print(f"Min in Tuple: {min(tuple_var[:3])}")  # Output: 1

# sum() - returns the sum of elements in a collection (only numeric)
print(f"Sum of List Elements: {sum(list_var[:3])}")  # Output: 6

# =====================
# 6. String Manipulations
# =====================

# String Concatenation
concat_str = "Hello" + " " + "World!"
print(f"Concatenated String: {concat_str}")

# String Formatting with f-strings
name = "Alice"
age = 25
formatted_str = f"My name is {name} and I am {age} years old."
print(f"Formatted String: {formatted_str}")

# String Methods
upper_str = str_var.upper()
print(f"Uppercase String: {upper_str}")  # Output: HELLO, WORLD!

# Finding a substring
substring_index = str_var.find("World")
print(f"Index of 'World': {substring_index}")  # Output: 7

# =====================
# End of data_types.py
# =====================

