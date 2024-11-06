# functions.py
# This file demonstrates defining and using functions in Python.

# =====================
# 1. Basic Function Definition
# =====================

# Define a simple function with no parameters
def greet():
    """Function to print a greeting message."""
    print("Hello, World!")

greet()  # Call the function

# Define a function with parameters
def add(a, b):
    """Function to add two numbers."""
    return a + b

result = add(3, 5)
print(f"Addition Result: {result}")  # Output: 8

# =====================
# 2. Default Parameters
# =====================

def greet_person(name="Guest"):
    """Function with a default parameter."""
    print(f"Hello, {name}!")

greet_person("Alice")  # Output: Hello, Alice!
greet_person()         # Output: Hello, Guest!

# =====================
# 3. Keyword Arguments
# =====================

def describe_person(name, age):
    """Function using keyword arguments."""
    print(f"Name: {name}, Age: {age}")

describe_person(age=25, name="Bob")  # Using keyword arguments

# =====================
# 4. Variable-Length Arguments
# =====================

# *args - captures extra positional arguments as a tuple
def sum_all(*args):
    """Function to sum all arguments."""
    return sum(args)

print(f"Sum of Arguments: {sum_all(1, 2, 3, 4)}")  # Output: 10

# **kwargs - captures extra keyword arguments as a dictionary
def print_info(**kwargs):
    """Function to print keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Charlie", age=30, city="New York")

# =====================
# 5. Lambda Functions (Anonymous Functions)
# =====================

# Lambda function for adding two numbers
add_lambda = lambda x, y: x + y
print(f"Lambda Addition Result: {add_lambda(5, 7)}")  # Output: 12

# Lambda function for square of a number
square = lambda x: x**2
print(f"Lambda Square Result: {square(4)}")  # Output: 16

# =====================
# 6. Higher-Order Functions
# =====================

# Passing a function as an argument
def apply_operation(x, y, func):
    """Function that applies a given operation to x and y."""
    return func(x, y)

# Using a lambda function as the operation
result = apply_operation(3, 4, lambda a, b: a * b)
print(f"Multiplication with Higher-Order Function: {result}")  # Output: 12

# =====================
# 7. Nested Functions and Closures
# =====================

def outer_function(message):
    """Outer function that defines an inner function."""
    def inner_function():
        print(f"Message: {message}")
    return inner_function  # Returns the inner function as a closure

my_func = outer_function("Hello from closure!")
my_func()  # Output: Message: Hello from closure!

# =====================
# 8. Recursion
# =====================

# Recursive function to calculate factorial of a number
def factorial(n):
    """Recursive function to calculate factorial."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(f"Factorial of 5: {factorial(5)}")  # Output: 120

# =====================
# 9. Decorators
# =====================

def my_decorator(func):
    """Decorator function to modify behavior of another function."""
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# =====================
# 10. Docstrings
# =====================

def example_function():
    """
    Example function with a docstring.

    This function demonstrates how to use docstrings for documentation.
    """
    print("This is an example function.")

# Accessing docstring
print(example_function.__doc__)

# =====================
# End of functions.py
# =====================
