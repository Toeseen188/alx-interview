#!/usr/bin/python3
"""
    implement a pascal trianlge
"""


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]  # Start each row with 1

        for j in range(1, i):
            # Calculate the value using the previous row
            value = triangle[i-1][j-1] + triangle[i-1][j]
            row.append(value)

        row.append(1)  # End each row with 1
        triangle.append(row)

    return triangle
