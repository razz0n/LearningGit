from new_file import solution

def get_matrix_solution() -> list[list[int]]:
    print("Checks whether the rows and columns in the matrix have all the number in the range n")
    rows: int = int(input("Enter the number of rows in the matrix"))
    columns: int = int(input("Enter the number of columns in the matrix"))
    matrix = get_user_input(rows,columns)
    return matrix

def get_user_input(rows: int,columns: int) -> list[list[int]]:
    matrix = [[] for i in range(rows)
    for i in range(len(rows)):
        for j in range(len(columns)):
            element: int = int(input("Enter the {}{}th element in the matrix".format(i+1,j+1)))
            matrix[i].append(element)
    return matrix

if __name__ == '__main__':
    start_matrix = get_matrix_solution()
    if solution(start_matrix):
        print("The matrix is valid")
    else:
        print("The matrix is not valid")
