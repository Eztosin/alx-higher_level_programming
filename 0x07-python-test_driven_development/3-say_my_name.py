#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """function that prints names given as parameters"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("{}".format("My name is"), end=" ")
        print("{} {}".format(first_name, last_name))
