#!/usr/bin/python3
"""contains a class Student that defines student"""


class Student:
    """defines a student"""
    def __init__(self, first_name, last_name, age):
        """initializing the attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a student"""
        return self.__dict__
