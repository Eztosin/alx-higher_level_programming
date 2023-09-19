#!/usr/bin/python3
"""Square module inherits from Rectangle class"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """a square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializing the attributes"""
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter method to get the size of the square"""
        return self.__width

    @size.setter
    def size(self, value):
        """setter method to set the size of the square"""
        if isinstance(value, bool):
            raise TypeError("width must be an integer")
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value
        self.__height = value

    def __str__(self):
        """returns a string representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.size)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args:
            if len(args) >= 1 and args[0] is not None:
                self.id = args[0]
            else:
                self.id
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
