# control_flow.py
# This file demonstrates control flow in Python, including conditionals and loops.

# =====================
# 1. Conditional Statements
# =====================

# if-elif-else statement
age = 20
if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")

# Short-hand if statement (one-liner)
num = 5
print("Positive") if num > 0 else print("Negative or Zero")

# Using logical operators in conditions
x = 10
y = 20
if x > 5 and y < 25:
    print("Both conditions are True")  # Output: Both conditions are True

# =====================
# 2. Looping Statements
# =====================

# For loop - iterates over a sequence (e.g., list, range, string)
for i in range(5):  # range(5) generates numbers from 0 to 4
    print(f"For Loop - Iteration {i}")

# Looping over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# Looping over a dictionary
person = {"name": "Alice", "age": 25}
for key, value in person.items():
    print(f"{key}: {value}")

# While loop - continues until the condition becomes False
count = 0
while count < 3:
    print(f"While Loop - Count: {count}")
    count += 1  # Increment count to avoid infinite loop

# =====================
# 3. Break and Continue Statements
# =====================

# Break - exits the loop completely
for i in range(5):
    if i == 3:
        break  # Loop will exit when i equals 3
    print(f"Break Example - i: {i}")

# Continue - skips the current iteration and moves to the next
for i in range(5):
    if i == 2:
        continue  # Skips the iteration when i equals 2
    print(f"Continue Example - i: {i}")

# =====================
# 4. Else with Loops
# =====================

# For loop with else - the else block executes when the loop completes normally (without `break`)
for i in range(3):
    print(f"Loop Else Example - i: {i}")
else:
    print("For loop completed without break")

# While loop with else
count = 0
while count < 3:
    print(f"While Loop Else - Count: {count}")
    count += 1
else:
    print("While loop completed without break")

# =====================
# 5. Nested Loops
# =====================

# Using nested for loops
for i in range(3):
    for j in range(2):
        print(f"Nested Loop - i: {i}, j: {j}")

# =====================
# 6. Pass Statement
# =====================

# pass - does nothing, used as a placeholder for future code
for i in range(3):
    if i == 1:
        pass  # Placeholder for code to be added later
    print(f"Pass Example - i: {i}")

# =====================
# 7. List Comprehension
# =====================

# List comprehension - a concise way to create lists
squares = [x**2 for x in range(5)]
print(f"Squares: {squares}")  # Output: [0, 1, 4, 9, 16]

# Conditional list comprehension
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"Even Squares: {even_squares}")  # Output: [0, 4, 16, 36, 64]

# =====================
# End of control_flow.py
# =====================
