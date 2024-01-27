#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    m = len(matrix)
    n = len(matrix[0])
    result = []
    for a in range(m):
        ans = list(map(lambda x: x * x, matrix[a]))
        result.append(ans)
    return result
