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


# ---------------- Main