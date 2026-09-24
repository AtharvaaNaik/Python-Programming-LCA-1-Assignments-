# Program to create arrays and perform addition of two matrices

def create_matrix(rows, cols, matrix_name):
    """Function to accept matrix elements from the user"""
    matrix = []
    print(f"\nEnter elements for {matrix_name} ({rows}x{cols}):")
    for i in range(rows):
        row = []
        for j in range(cols):
            value = int(input(f"Enter element [{i}][{j}]: "))
            row.append(value)
        matrix.append(row)
    return matrix


def add_matrices(matrix1, matrix2, rows, cols):
    """Function to add two matrices"""
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result


def display_matrix(matrix, name):
    """Function to display a matrix"""
    print(f"\n{name}:")
    for row in matrix:
        print(row)


# ---------------- Main ----------------
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix1 = create_matrix(rows, cols, "Matrix 1")
matrix2 = create_matrix(rows, cols, "Matrix 2")

result = add_matrices(matrix1, matrix2, rows, cols)

display_matrix(matrix1, "Matrix 1")
display_matrix(matrix2, "Matrix 2")
display_matrix(result, "Sum of Matrices")