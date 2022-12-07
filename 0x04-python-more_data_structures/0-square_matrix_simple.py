#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    for row in new_matrix:
        for i in row:
            print(i)
            i = i * i
            print(i)
    return new_matrix
