#!/usr/bin/python3
"""Base module"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if not (isinstance(list_dictionaries, list) or not
                all(isinstance(i, dict) for i in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list "
                            "of dictionaries")
        return json.dumps(list_dictionaries)
