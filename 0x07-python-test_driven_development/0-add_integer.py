#!/usr/bin/python3
"""This module contains a function that adds 2 integers"""


def add_integer(a, b=98):
    """ Function that adds 2 integers
    Args:
        a (int or float): First argument
        b (int or float, optional parameter): Second argument

    Returns:
         int: The sum of parameter a and b
    """

    if (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        x = int(a)
        y = int(b)
        return (x + y)
    elif not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
