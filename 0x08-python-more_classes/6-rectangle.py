#!/usr/bin/python3
"""Defining a rectangle"""


class Rectangle:
    """a class that defines a rectangle"""
    number_of_instances = 0
    
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
        Rectangle.number_of_instances += 1

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

    def area(self):
        """returns the area of the rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (self.__height + self.__width) * 2

    def __str__(self):
        """prints the rectangle with the character "#" """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_str = ""
        for _ in range(self.__height):
            rect_str += "#" * self.__width + "\n"
        return rect_str[:-1]

    def __repr__(self):
        """returns a string representation of the rectangle
        to be able to create a new instance by using eval()

        """
        return "Rectangle({:d}, {:d})".format(self.__width,
                                              self.__height)

    def __del__(self):
        """prints a message if an instance is deleted"""
        print("{}".format("Bye rectangle..."))
        Rectangle.number_of_instances -= 1
