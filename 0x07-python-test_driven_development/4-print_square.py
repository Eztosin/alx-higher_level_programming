#!/usr/bin/python3
"""Prints a square"""


def print_square(size):
    """
    Prints a square with the character '#'

    Args:
        size is the length of the square

    Return:
         a square printed to stdout

    Raises:
         TypeError: If size is not an integer
         TypeError: If size is a float and is less than 0
         ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if (isinstance(size, float)) < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("{}".format("#" * size))
