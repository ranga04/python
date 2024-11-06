# error_handling.py
# This file demonstrates exception handling in Python.

# =====================
# 1. Basic Try-Except
# =====================

# Handling a division by zero error
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# Handling a type error
try:
    result = "string" + 10
except TypeError:
    print("Error: Cannot add string and integer!")

# =====================
# 2. Catching Multiple Exceptions
# =====================

# Using multiple except blocks
try:
    number = int("abc")  # This will raise a ValueError
    result = 10 / 0      # This will raise a ZeroDivisionError if reached
except ValueError:
    print("Error: Invalid conversion to integer!")
except ZeroDivisionError:
    print("Error: Division by zero!")

# =====================
# 3. Catching Multiple Exceptions in One Block
# =====================

try:
    number = int("abc")
except (ValueError, TypeError) as e:
    print(f"Error occurred: {e}")

# =====================
# 4. Else Clause
# =====================

# Using else with try-except
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Division successful, result is: {result}")  # Output: 5.0

# =====================
# 5. Finally Clause
# =====================

# Finally block will always execute, regardless of exception
try:
    file = open("example.txt", "w")
    file.write("Hello, World!")
except IOError:
    print("An error occurred while writing to the file.")
finally:
    file.close()  # This will always execute, ensuring the file is closed
    print("File closed.")

# =====================
# 6. Raising Exceptions
# =====================

# Using `raise` to throw an exception manually
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    print(f"Valid age: {age}")

try:
    check_age(-1)
except ValueError as e:
    print(f"Exception caught: {e}")

# =====================
# 7. Custom Exceptions
# =====================

# Creating a custom exception by inheriting from Exception
class NegativeNumberError(Exception):
    """Custom exception for negative numbers."""
    pass

def square_root(number):
    if number < 0:
        raise NegativeNumberError("Cannot take square root of a negative number!")
    return number ** 0.5

try:
    print(square_root(-9))
except NegativeNumberError as e:
    print(f"Custom Exception Caught: {e}")

# =====================
# 8. Assertions
# =====================

# Using assertions to ensure conditions are met
def divide(a, b):
    assert b != 0, "Denominator cannot be zero"
    return a / b

try:
    print(divide(10, 0))
except AssertionError as e:
    print(f"Assertion Error: {e}")

# =====================
# End of error_handling.py
# =====================
