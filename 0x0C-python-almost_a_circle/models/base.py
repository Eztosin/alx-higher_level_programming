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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                new_list = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None and json_string == "":
            return "[]"
        if not isinstance(json_string, str):
            raise TypeError("json_string must be a string")
        return (json.loads(json_string))
