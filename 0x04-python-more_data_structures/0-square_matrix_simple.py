#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    for x in range(len(new_matrix)):
        new_matrix[x] = matrix[x].copy()
        for i in range(len(new_matrix[x])):
            print(new_matrix[x][i])
            new_matrix[x][i] = new_matrix[x][i] * new_matrix[x][i]
            print(new_matrix[x][i])
    return new_matrix
