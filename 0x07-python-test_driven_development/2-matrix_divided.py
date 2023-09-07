#!/usr/bin/python3
"""divides elements of a matrix"""


def matrix_divided(matrix, div):

    """
    A function that divides all elements of a matrix

    Args:
       matrix must be a list of lists of integers floats.
       div must be a number(integer or float).

    Return:
        a new matrix of the computation.

    Raises:
        TypeError: if matrix is not a list of lists(integers or floats)
        TypeError: if div is not an integer or float.
        TypeError: if row is not of the same size.
        ZeroDivisionError: if div is equal to zero.
    """

    result_matrix = []
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have "
                        "the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        result = [round(val / div, 2) for val in row]
        result_matrix.append(result)

    return result_matrix
