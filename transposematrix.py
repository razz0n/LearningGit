def transpose(matrix: list[list[int]]) -> list[list[int]]:
    rows: int = len(matrix)
    cols: int = len(matrix[0])
    transpose_matrix: list[list[int]] = [[] for i in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transpose_matrix.append(matrix[j][i])

    return transpose_matrix

print(transpose([[1,2,3],[3,2,4]]))