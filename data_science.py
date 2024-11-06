# data_science.py
# This file demonstrates the basics of data manipulation and analysis using pandas and numpy.

# =====================
# 1. NumPy Library
# =====================

import numpy as np

# Creating a NumPy array
array = np.array([1, 2, 3, 4, 5])
print("NumPy Array:", array)

# Array operations
print("Array multiplied by 2:", array * 2)        # Element-wise multiplication
print("Array squared:", array ** 2)               # Element-wise squaring
print("Sum of Array Elements:", np.sum(array))    # Sum of all elements

# Multi-dimensional arrays
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array (Matrix):\n", matrix)
print("Transpose of Matrix:\n", np.transpose(matrix))

# Generating arrays with specific ranges and shapes
zeros_array = np.zeros((2, 3))
ones_array = np.ones((2, 3))
range_array = np.arange(0, 10, 2)   # Array with step size
print("Zeros Array:\n", zeros_array)
print("Ones Array:\n", ones_array)
print("Range Array:", range_array)

# =====================
# 2. Pandas Library
# =====================

import pandas as pd

# Creating a DataFrame from a dictionary
data = {
    "Name": ["Alice", "Bob", "Cathy"],
    "Age": [24, 27, 22],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

# Accessing columns and rows
print("Names Column:\n", df["Name"])
print("First Row:\n", df.iloc[0])

# Adding a new column
df["Salary"] = [70000, 80000, 75000]
print("DataFrame with Salary Column:\n", df)

# Filtering data
adults = df[df["Age"] > 23]
print("Filtered Data (Age > 23):\n", adults)

# Descriptive statistics
print("Statistics:\n", df.describe())

# =====================
# 3. Data Manipulation
# =====================

# Renaming columns
df = df.rename(columns={"City": "Location"})
print("DataFrame with Renamed Column:\n", df)

# Handling missing data
df.loc[3] = ["David", 29, None, 65000]  # Add a row with missing Location
print("DataFrame with Missing Value:\n", df)
df["Location"].fillna("Unknown", inplace=True)  # Fill missing values
print("DataFrame after Filling Missing Values:\n", df)

# Grouping data
grouped = df.groupby("Location")["Salary"].mean()
print("Average Salary by Location:\n", grouped)

# =====================
# 4. Reading and Writing Data
# =====================

# Writing DataFrame to CSV
df.to_csv("data.csv", index=False)
print("DataFrame saved to 'data.csv'.")

# Reading DataFrame from CSV
df_from_csv = pd.read_csv("data.csv")
print("DataFrame loaded from CSV:\n", df_from_csv)

# =====================
# 5. Merging and Joining Data
# =====================

# Creating another DataFrame to merge
extra_data = pd.DataFrame({
    "Name": ["Alice", "Bob", "Eve"],
    "Department": ["HR", "Finance", "Engineering"]
})

# Merging DataFrames on a common column
merged_df = pd.merge(df, extra_data, on="Name", how="left")
print("Merged DataFrame:\n", merged_df)

# =====================
# End of data_science.py
# =====================
