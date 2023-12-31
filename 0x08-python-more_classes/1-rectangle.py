#!/usr/bin/python3
"""Defining a rectangle"""


class Rectangle:
    """a class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """initializing the class object attributes
        Args:
            width: the width of the rectangle
            height: the height of the rectangle
        Raises:
             TypeError: If the value of the width or height is not
                        an integer.
             ValueError: If the value of the width or height is
                         less than 0.

        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """getter method to retrieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method to set the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter method to retrieve the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method to set the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
