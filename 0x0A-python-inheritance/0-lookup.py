#!/usr/bin/python3
""" this module prints the list od available attributes"""


def lookup(obj):
    """returns the list of available attributes
    and methods of an object"""
    return dir(obj)
