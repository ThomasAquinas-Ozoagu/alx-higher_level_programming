#!/usr/bin/python3
"""
Prototype: def matrix_divided(matrix, div):
matrix must be a list of lists of integers or floats, otherwise raise a
TypeError exception with the message matrix must be a matrix (list of
lists) of integers/floats
Each row of the matrix must be of the same size, otherwise raise a
TypeError exception with the message Each row of the matrix must have
the same size
div must be a number (integer or float), otherwise raise a TypeError
exception with the message div must be a number
div can’t be equal to 0, otherwise raise a ZeroDivisionError exception
with the message division by zero
All elements of the matrix should be divided by div, rounded to 2 decimal
places
Returns a new matrix
You are not allowed to import any module
"""


def matrix_divided(matrix, div):
    """
    a function that divides all elements of a matrix.
    """
    """ Checks if matrix is a list of integers or floats """
    for a in range(len(matrix)):
        if type(matrix[a]) != list:
            raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    for a in range(len(matrix)):
        for b in range(len(matrix[a])):
            if type(matrix[a][b]) != int and type(matrix[a][b]) != float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

    """ Checks if every row is the same size """
    rowlen = len(matrix[0])
    for a in range(len(matrix)):
        if len(matrix[a]) != rowlen:
            raise TypeError("Each row of the matrix must have the same size")
    """checks if div is a number """
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    """checks if div is zero """
    if div == 0:
        raise ZeroDivisionError("division by zero")

    """ create new_matrix of equal dimension """
    newmat = []
    for a in range(len(matrix)):
        newmat.append(matrix[a][:])

    """ modify new_matrix to contain the elements of matrix divided by 2"""
    for a in range(len(matrix)):
        for b in range(len(matrix[a])):
            newmat[a][b] = round(matrix[a][b]/div, 2)

    return newmat
