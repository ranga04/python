# file_handling.py
# This file demonstrates reading from and writing to files in Python.

# =====================
# 1. Writing to a File
# =====================

# Writing text to a file in write mode ('w')
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a new line.\n")

# =====================
# 2. Appending to a File
# =====================

# Appending text to an existing file
with open("example.txt", "a") as file:
    file.write("Appending a new line.\n")

# =====================
# 3. Reading from a File
# =====================

# Reading the entire content of a file
with open("example.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)

# =====================
# 4. Reading Line by Line
# =====================

# Reading a file line by line using a loop
with open("example.txt", "r") as file:
    for line in file:
        print("Line:", line.strip())  # strip() removes trailing newline characters

# =====================
# 5. Reading Specific Number of Characters
# =====================

# Reading only the first 5 characters
with open("example.txt", "r") as file:
    partial_content = file.read(5)
    print("First 5 Characters:", partial_content)

# =====================
# 6. File Modes
# =====================

# Modes for opening files:
# 'r'  - read (default mode)
# 'w'  - write (overwrites the file if it exists)
# 'a'  - append (adds to the end of the file)
# 'r+' - read and write
# 'w+' - write and read (overwrites the file if it exists)
# 'a+' - append and read

# Demonstrating read and write mode
with open("example.txt", "r+") as file:
    file.write("Overwriting at the beginning of the file.\n")
    file.seek(0)  # Move cursor back to the beginning
    content = file.read()
    print("Modified Content:\n", content)

# =====================
# 7. Working with Binary Files
# =====================

# Writing binary data (useful for images, audio files, etc.)
with open("binary_example.bin", "wb") as file:
    file.write(b"This is binary data.")

# Reading binary data
with open("binary_example.bin", "rb") as file:
    binary_content = file.read()
    print("Binary Content:", binary_content)

# =====================
# 8. Using the `os` Module for File Operations
# =====================

import os

# Check if a file exists
if os.path.exists("example.txt"):
    print("example.txt exists.")
else:
    print("example.txt does not exist.")

# Renaming a file
os.rename("example.txt", "renamed_example.txt")
print("File renamed to renamed_example.txt")

# Deleting a file
os.remove("binary_example.bin")
print("binary_example.bin has been deleted.")

# =====================
# 9. Working with Directories
# =====================

# Creating a new directory
os.mkdir("new_directory")

# Listing files and directories
print("Directory Contents:", os.listdir("."))

# Deleting a directory
os.rmdir("new_directory")
print("new_directory has been deleted.")

# =====================
# End of file_handling.py
# =====================
