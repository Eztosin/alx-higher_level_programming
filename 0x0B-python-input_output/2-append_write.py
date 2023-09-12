#!/usr/bin/python3
"""contains a function that appends a string at the end of a file"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file
    and returns the number of characters added
    """
    with open(filename, "a") as file:
        file.write(text)
    return len(text)
