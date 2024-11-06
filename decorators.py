# decorators.py
# This file demonstrates how to use decorators in Python.

# =====================
# 1. Basic Decorator
# =====================

# Defining a simple decorator
def simple_decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

# Applying the decorator to a function
@simple_decorator
def greet():
    print("Hello!")

greet()  # Output will include messages before and after "Hello!"

# =====================
# 2. Decorator with Arguments
# =====================

def repeat_decorator(num_repeats):
    """Decorator to repeat a function multiple times."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_repeats):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat_decorator(3)  # This will repeat the function 3 times
def say_hello():
    print("Hello!")

say_hello()  # Output: "Hello!" repeated 3 times

# =====================
# 3. Decorators for Logging
# =====================

def log_decorator(func):
    """Decorator that logs function calls."""
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned: {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

add(3, 4)  # Logs the call and result of the function

# =====================
# 4. Decorators with Function Metadata
# =====================

from functools import wraps

def preserve_metadata_decorator(func):
    """Decorator that preserves metadata of the wrapped function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@preserve_metadata_decorator
def example_function():
    """This is an example function."""
    print("Example function is running.")

print(f"Function name: {example_function.__name__}")  # Output: example_function
print(f"Function docstring: {example_function.__doc__}")  # Output: This is an example function.

# =====================
# 5. Practical Example: Timing Decorator
# =====================

import time

def timer_decorator(func):
    """Decorator that times the execution of a function."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds to execute.")
        return result
    return wrapper

@timer_decorator
def slow_function():
    time.sleep(2)  # Simulating a slow function
    print("Slow function completed.")

slow_function()  # Output: slow_function took ~2.0000 seconds to execute.

# =====================
# 6. Practical Example: Authorization Decorator
# =====================

def authorized(func):
    """Decorator that checks if a user is authorized."""
    def wrapper(user, *args, **kwargs):
        if user.get("is_admin"):
            return func(*args, **kwargs)
        else:
            print("Unauthorized access!")
    return wrapper

@authorized
def secret_function():
    print("Accessing a protected resource.")

user = {"username": "john", "is_admin": True}
secret_function(user)  # Output: Accessing a protected resource.

user = {"username": "jane", "is_admin": False}
secret_function(user)  # Output: Unauthorized access!

# =====================
# End of decorators.py
# =====================
