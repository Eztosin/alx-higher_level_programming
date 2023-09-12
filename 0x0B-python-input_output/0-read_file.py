#!/usr/bin/python3
"""contains a function that reads a text file"""


def read_file(filename=""):
    """reads a text file and prints it to standard output"""
    with open(filename, "r") as file:
        for line in file:
            print(line, end="")
