import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    
    rows = len(A)
    cols = len(A[0])

    transpose_matrix = np.zeros((cols,rows))
    
    for row in range(rows):
        for col in range(cols):
            transpose_matrix[col][row] = A[row][col]
    
    return transpose_matrix

    
