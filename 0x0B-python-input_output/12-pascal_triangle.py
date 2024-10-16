#!/usr/bin/python3
"""Module to generate Pascal's Triangle."""


def pascal_triangle(n):
    """Creates a list of lists representing Pascal's Triangle up to row n."""
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row

    for i in range(1, n):
        row = [1]  # First element of the row is always 1
        last_row = triangle[-1]  # Get the last row from the triangle
        
        # Compute the values in the current row
        for j in range(1, i):
            row.append(last_row[j - 1] + last_row[j])
        
        row.append(1)  # Last element of the row is always 1
        triangle.append(row)  # Add the current row to the triangle

    return triangle
