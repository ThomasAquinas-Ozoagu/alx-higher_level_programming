#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    size = len(matrix[0])
    for i in range(len(matrix)):
        for j in range(size):
            print("{:d}".format(matrix[i][j]),
                  end=" " if j < (size - 1) else "")
        print()
