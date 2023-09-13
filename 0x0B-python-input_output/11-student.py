#!/usr/bin/python3
"""contains a class Student that defines student"""


class Student:
    """defines a student"""
    def __init__(self, first_name, last_name, age):
        """initializing the attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a student
        if attrs is a list of strings, only attribute names contained
        in the list should be retrieved.

        """
        if attrs is None:
            return self.__dict__
        if isinstance(attrs, list) and all(isinstance(attr, str)
                                           for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of student"""
        for key, value in json.items():
            setattr(self, key, value)
