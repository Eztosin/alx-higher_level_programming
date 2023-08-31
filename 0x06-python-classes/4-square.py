#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """creates an instance of the square class
    and assigns it to the variable size"""

    def __init__(self, size=0):

        """Initializing size with the required error checks"""
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be an >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area"""
        return (self.size ** 2)
