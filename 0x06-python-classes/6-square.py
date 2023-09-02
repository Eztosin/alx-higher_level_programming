#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """creates an instance of the square class
    and assigns it to the variable size"""

    def __init__(self, size=0, position=(0, 0)):

        """Initializing size with the required error checks"""
        self.size = size
        self.position = position

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
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter method to retrieve position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method to set the position"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of "
                            "2 positive integers")
        for i in value:
            if not isinstance(i, int) or i < 0:
                raise TypeError("position must be a tuple of "
                                "2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area"""
        return (self.size ** 2)

    def my_print(self):
        """Prints in standard output the square using
        the '#' character"""

        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                if self.__position[0] > 0:
                    print("{}".format(" " * self.__position[0]),
                          end='')
                print("{}".format("#" * self.__size))
