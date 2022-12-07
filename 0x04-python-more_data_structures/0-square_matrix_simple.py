#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    for row in new_matrix:
        row = row.copy()
        for i in range(len(row)):
            print(i)
            row[i] = row[i] * row[i]
            print(i)
    return new_matrix
