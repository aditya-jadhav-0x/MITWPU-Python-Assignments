# ==========================================
# PART A: MATRIX ADDITION USING PYTHON LISTS
# ==========================================
print("--- Matrix Addition using standard Python Lists ---")

# Taking dimensions from the user
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Initialize empty lists for the matrices
matrix1 = []
matrix2 = []

# Input for Matrix 1
print("\nEnter elements for Matrix 1:")
for i in range(rows):
    row_elements = []
    for j in range(cols):
        val = int(input(f"Enter element at position ({i},{j}): "))
        row_elements.append(val)
    matrix1.append(row_elements)

# Input for Matrix 2
print("\nEnter elements for Matrix 2:")
for i in range(rows):
    row_elements = []
    for j in range(cols):
        val = int(input(f"Enter element at position ({i},{j}): "))
        row_elements.append(val)
    matrix2.append(row_elements)

# Initialize a result matrix filled with zeros
result_list = []
for i in range(rows):
    row_zeros = []
    for j in range(cols):
        row_zeros.append(0)
    result_list.append(row_zeros)

# Perform addition using nested loops
for i in range(rows):
    for j in range(cols):
        result_list[i][j] = matrix1[i][j] + matrix2[i][j]

# Displaying the result
print("\nResultant Matrix after Addition (Using Lists):")
for row in result_list:
    print(row)


# ==========================================
# PART B: MATRIX ADDITION USING NUMPY ARRAY
# ==========================================
print("\n--- Matrix Addition using NumPy Array ---")
import numpy as np

# Convert the previously entered lists into NumPy arrays
array1 = np.array(matrix1)
array2 = np.array(matrix2)

print("\nMatrix 1 as NumPy Array:")
print(array1)

print("\nMatrix 2 as NumPy Array:")
print(array2)

# NumPy allows direct addition without any loops
result_numpy = array1 + array2

print("\nResultant Matrix after Addition (Using NumPy):")
print(result_numpy)
