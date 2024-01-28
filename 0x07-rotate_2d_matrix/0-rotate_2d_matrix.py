#!/usr/bin/python3
""" The method to rotate a 2d matrix in 90 degrees
"""


def rotate_2d_matrix(matrix):
    """ Rotate 2-Dimensional matrix to 90 degrees """
    n = len(matrix)

    # transpose by swapping the columns element with rows elements
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # then we reverse the matrix to achieve a full 90 degree rotation
    for i in range(n):
        matrix[i].reverse()
