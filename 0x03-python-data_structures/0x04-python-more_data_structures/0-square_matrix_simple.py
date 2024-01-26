#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    x = len(matrix)
    y = len(matrix[0])
    rows = []
    for n in range(x):
        cols = []
        for m in range(y):
            cols.append(matrix[n][m] * matrix[n][m])
        rows.append(cols)
    return rows
