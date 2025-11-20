import numpy as np

# Creating matrices using NumPy arrays
matrix1 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

matrix2 = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

# Matrix addition
result_add = matrix1 + matrix2
print("Matrix Addition Result (NumPy):")
print(result_add)

# Matrix multiplication
result_multiply = np.dot(matrix1, matrix2) # Or matrix1 @ matrix2 (Python 3.5+)
print("Matrix Multiplication Result (NumPy):")
print(result_multiply)

# Transpose a matrix
transposed_matrix = matrix1.T
print("Transposed Matrix (NumPy):")
print(transposed_matrix)
