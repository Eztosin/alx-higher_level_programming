#!/usr/bin/python3
"""contains a function that writes to a file"""


def write_file(filename="", text=""):
    """writes a string to a text file and returns
    the number of characters written.

    """
    with open(filename, "w") as file:
        no_of_chars = file.write(text)
    return (no_of_chars)
