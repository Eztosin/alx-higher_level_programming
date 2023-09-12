#!/usr/bin/python3
"""contains a class that inherits from BaseGeometry"""


class BaseGeometry:
    """class contains an empty area method
    Raises: Exception
            TypeError: If value is not an integer
            ValueError: If value is less or equal to 0
    """

    def integer_validator(self, name, value):
        """validates the value"""
        self.name = name
        self.value = value
        if type(value) != int:
            raise TypeError("{}".format(name + " must be an integer"))
        if value <= 0:
            raise ValueError("{}".format(name + " must be greater "
                                         "than 0"))


class Rectangle(BaseGeometry):
    """a class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """initializing the class object attributes
        Args:
            width: the width of the rectangle
            height: the height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return (self.__height * self.__width)

    def __str__(self):
        """prints the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
