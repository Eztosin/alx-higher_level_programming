#!/usr/bin/python3
"""Checks if an object is an instance of a spcified class"""


def is_kind_of_class(obj, a_class):
    """Returns true if an object is an instance of the class

    Args:
        obj: object
        a_class: class

    Return: True if object is an instance of the class
            False: If object is not an instance of the class
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
