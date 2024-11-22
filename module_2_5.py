def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix_row = []
        for j in range(m):
                matrix_row.append(value)
        matrix.append(matrix_row)
    return matrix

result = get_matrix(4,2 ,13)
print(result)