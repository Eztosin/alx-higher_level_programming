#!/usr/bin/python3
"""Base module"""


class Base:
    """Base class to manage id attribute"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing an instance of Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
