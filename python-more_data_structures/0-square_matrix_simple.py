#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = [list(map(lambda x: x**2, row)) for row in matrix]
    return (newmatrix)
