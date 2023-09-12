#!/usr/bin/python3
"""contains a function that returns a dictionary description
   with simple data structure
"""


def class_to_json(obj):
    """returns a dictionary description with simple data structure
    for JSON serialization of an object

    """
    return obj.__dict__
