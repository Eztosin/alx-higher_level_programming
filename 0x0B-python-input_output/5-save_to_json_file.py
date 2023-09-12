#!/usr/bin/python3
"""contains a function that writes an object to a text file
 using JSON """
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file, using a JSON
    representation
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
