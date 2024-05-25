def solution(matrix: list[list[int]]) -> bool:
    n = len(matrix)
    row_list = []
    rule = [x for x in range(1, n + 1)]
    for row in matrix:
        for i in range(len(row)):
            row_list.append(row[i])

        if set(row_list) != set(rule):
            return False
        row_list.clear()

    col = [[] for _ in range(len(matrix[0]))]

    print(col)
    for i in range(n):
        for j in range(n):
            col[j].append(matrix[i][j])

    print(col)
    return all(set(column) == set(rule) for column in col)

