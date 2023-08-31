#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """creates an instance of the square class
    and assigns it to the variable size"""

    def __init__(self, size=0):

        """Checking if size is a valid integer and or less than
        zero"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be an >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2
