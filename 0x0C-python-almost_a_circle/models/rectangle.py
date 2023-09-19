#!/usr/bin/python3
"""Rectangle module inherits from Base class"""
from models.base import Base


class Rectangle(Base):
    """a rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializing the attributes"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter method to get the width of the rectangle"""
        return self.__width

    @property
    def height(self):
        """getter method to get the height of the rectangle"""
        return self.__height

    @property
    def x(self):
        """getter method to get the x coordinate of the rectangle"""
        return self.__x

    @property
    def y(self):
        """getter method to get the y coordinate of the rectangle"""
        return self.__y

    @width.setter
    def width(self, value):
        """setter method to set the width of the rectangle"""
        if isinstance(value, bool):
            raise TypeError("width must be an integer")
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """setter method to set the height of the rectangle"""
        if isinstance(value, bool):
            raise TypeError("height must be an integer")
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @x.setter
    def x(self, value):
        """setter method to set the x coordinate of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @y.setter
    def y(self, value):
        """setter method to set the y coordinate of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """returns the area of the rectangle"""
        return (self.__height * self.__width)

    def display(self):
        """displays to standard output the rectangle
           using "#" symbol

        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print("{} {}".format(" " * self.__x, "#" * self.__width))

    def __str__(self):
        """returns a string representation of the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)