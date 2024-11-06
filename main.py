# main.py
# This file serves as the main script to demonstrate the usage of all other modules.

# Import statements for all the custom modules
import data_types
import control_flow
import functions
import classes_oop
import modules_and_packages
import error_handling
import file_handling
import standard_libraries
import data_science
import decorators
import concurrency

# =====================
# Main Execution
# =====================

print("=== Main Execution Script ===\n")

# Data Types and Structures
print("\n=== Data Types and Structures ===")
data_types.int_var = 42
print(f"Integer variable from data_types: {data_types.int_var}")
print(f"List from data_types: {data_types.list_var}")

# Control Flow
print("\n=== Control Flow ===")
control_flow.num = 10
control_flow.greet_person("Main Execution Script")

# Functions
print("\n=== Functions ===")
result = functions.add(10, 5)
print(f"Addition Result (Functions): {result}")
functions.say_hello()

# Classes and Object-Oriented Programming
print("\n=== Classes and OOP ===")
person = classes_oop.Person("Alice", 25)
person.greet()
employee = classes_oop.Employee("John", 60000)
print(f"Employee's Company: {employee.company}")

# Modules and Packages
print("\n=== Modules and Packages ===")
modules_and_packages.current_time = modules_and_packages.datetime.now()
print(f"Current Date and Time: {modules_and_packages.current_time}")

# Error Handling
print("\n=== Error Handling ===")
try:
    error_handling.check_age(-5)
except ValueError as e:
    print(f"Caught Exception in main.py: {e}")

# File Handling
print("\n=== File Handling ===")
with open("test_file.txt", "w") as file:
    file.write("This file was created by main.py\n")
print("File created successfully.")

# Standard Libraries
print("\n=== Standard Libraries ===")
print("Random Integer:", standard_libraries.random.randint(1, 10))
print("Pi from Math Library:", standard_libraries.math.pi)

# Data Science with Pandas and NumPy
print("\n=== Data Science ===")
import numpy as np
import pandas as pd
sample_array = np.array([10, 20, 30])
print(f"Sample NumPy Array: {sample_array}")
sample_df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
print("Sample DataFrame:\n", sample_df)

# Decorators
print("\n=== Decorators ===")
@decorators.timer_decorator
def example_function():
    print("Example function is running.")

example_function()

# Concurrency
print("\n=== Concurrency ===")
concurrency_thread = concurrency.threading.Thread(target=concurrency.print_numbers)
concurrency_thread.start()
concurrency_thread.join()

print("\n=== Main Script Completed ===")
