#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """
    method to sort out land from water
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Check only land cells
                perimeter += 4  # Initialize with 4 sides

                # Check left neighbor
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Subtract 2 if left neighbor is land

                # Check top neighbor
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Subtract 2 if top neighbor is land

    return perimeter
