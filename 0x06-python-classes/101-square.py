#!/usr/bin/python3
"""defines a class square"""


class Square:
    """creates an instance of the square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing the class with its attributes"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """gets the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """gets the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the position"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 "
                            "positive integer")
        for i in value:
            if not isinstance(i, int) or i < 0:
                raise TypeError("position must be a tuple of 2 "
                                "positive integer")
        self.__position = value

    def area(self):
        """returns the area of the square"""
        return (self.__size ** 2)

    def __str__(self):
        """String representation of the square"""

        result = []

        if self.__size == 0:
            return ""

        for _ in range(self.__position[1]):
            result.append("")

        for _ in range(self.__size):
            if self.__position[0] > 0:
                result.append(" " * self.__position[0] +
                              "#" * self.__size)
            else:
                result.append("#" * self.__size)

        return "\n".join(result)
