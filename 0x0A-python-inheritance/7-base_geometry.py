#!/usr/bin/python3
"""module contains a class based on 6-base_geometry.py"""


class BaseGeometry:
    """class contains an empty area method
    Raises: Exception
            TypeError: If value is not an integer
            ValueError: If value is less or equal to 0

    """
    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the value"""
        self.name = name
        self.value = value
        if type(value) != int:
            raise TypeError("{}".format(name + " must be an integer"))
        if value <= 0:
            raise ValueError("{}".format(name + " must be greater "
                            "than 0"))
