# Example: Creating a 3x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements
print(f"Element at (0,0): {matrix[0][0]}") # Output: 1
print(f"Element at (1,2): {matrix[1][2]}") # Output: 6

# Matrix addition using nested loops
matrix_a = [[1, 2], [3, 4]]
matrix_b = [[5, 6], [7, 8]]
result_matrix = [[0, 0], [0, 0]]

for i in range(len(matrix_a)):
    for j in range(len(matrix_a[0])):
        result_matrix[i][j] = matrix_a[i][j] + matrix_b[i][j]

print("Matrix Addition Result (Nested Lists):")
for row in result_matrix:
    print(row)
