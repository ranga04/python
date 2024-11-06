# standard_libraries.py
# This file demonstrates common Python libraries with examples.

# =====================
# 1. Math Library
# =====================

import math

# Using math functions
print(f"Square Root of 16: {math.sqrt(16)}")        # Output: 4.0
print(f"Exponential of 2: {math.exp(2)}")           # Output: ~7.389
print(f"Cosine of Pi: {math.cos(math.pi)}")         # Output: -1.0
print(f"Factorial of 5: {math.factorial(5)}")       # Output: 120

# Constants in math library
print(f"Pi Constant: {math.pi}")                    # Output: 3.14159...
print(f"Euler's Number (e): {math.e}")              # Output: 2.71828...

# =====================
# 2. Random Library
# =====================

import random

# Generating random numbers
print(f"Random Integer (1 to 10): {random.randint(1, 10)}")     # Random int between 1 and 10
print(f"Random Float (0 to 1): {random.random()}")              # Random float between 0 and 1

# Choosing a random element from a list
colors = ["red", "blue", "green", "yellow"]
print(f"Random Choice: {random.choice(colors)}")

# Shuffling a list randomly
random.shuffle(colors)
print(f"Shuffled List: {colors}")

# =====================
# 3. Datetime Library
# =====================

from datetime import datetime, timedelta

# Getting current date and time
now = datetime.now()
print(f"Current Date and Time: {now}")

# Formatting date and time
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted Date: {formatted_date}")

# Calculating a future date by adding days
future_date = now + timedelta(days=5)
print(f"Date 5 Days from Now: {future_date}")

# Parsing a date from a string
date_str = "2024-11-06"
parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
print(f"Parsed Date: {parsed_date}")

# =====================
# 4. JSON Library
# =====================

import json

# Creating a Python dictionary
data = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "is_student": False
}

# Converting dictionary to JSON
json_data = json.dumps(data)
print(f"JSON Data: {json_data}")

# Converting JSON back to dictionary
parsed_data = json.loads(json_data)
print(f"Parsed JSON Data: {parsed_data}")

# Writing JSON data to a file
with open("data.json", "w") as json_file:
    json.dump(data, json_file)

# Reading JSON data from a file
with open("data.json", "r") as json_file:
    loaded_data = json.load(json_file)
    print(f"Loaded Data from JSON File: {loaded_data}")

# =====================
# 5. OS Library
# =====================

import os

# Get the current working directory
cwd = os.getcwd()
print(f"Current Working Directory: {cwd}")

# List files and directories in the current directory
print("Directory Contents:", os.listdir(cwd))

# Check if a file exists
file_exists = os.path.exists("data.json")
print(f"Does 'data.json' Exist? {file_exists}")

# =====================
# 6. Sys Library
# =====================

import sys

# Print the Python version
print(f"Python Version: {sys.version}")

# Print command-line arguments (if any)
print(f"Command-Line Arguments: {sys.argv}")

# Exiting the script
# sys.exit()  # Uncomment to exit the program

# =====================
# 7. Time Library
# =====================

import time

# Get the current time in seconds since the Epoch
current_time = time.time()
print(f"Current Time (Seconds since Epoch): {current_time}")

# Pausing execution for a certain amount of time
print("Pausing for 2 seconds...")
time.sleep(2)
print("Resumed after pause.")

# Measuring execution time
start_time = time.time()
for i in range(1000000):
    pass
end_time = time.time()
print(f"Execution Time: {end_time - start_time} seconds")

# =====================
# End of standard_libraries.py
# =====================
