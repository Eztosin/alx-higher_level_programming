#!/usr/bin/python3
"""function that prints names given as parameters"""


def say_my_name(first_name, last_name=""):
    """function that prints names given as parameters
    Args:
        first_name: First parameter to function
        last_name: Second parameter to function initialized to ""

    Return:
         the parameters(string of chars) passed to function.

    Raises:
         TypeError: If first_name or last_name is not a string.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("{}".format("My name is"), end=" ")
        print("{} {}".format(first_name, last_name))
