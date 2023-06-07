def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Create a new matrix with switched dimensions
    transpose_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

    # Iterate through the original matrix and switch row and column indices
    for i in range(rows):
        for j in range(cols):
            transpose_matrix[j][i] = matrix[i][j]

    return transpose_matrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = transpose(matrix)
print(result)
