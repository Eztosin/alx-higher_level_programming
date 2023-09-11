#!/usr/bin/python3
"""this module defines a class that inherits from a list"""


class MyList(list):
    """inherits from lists"""

    def print_sorted(self):
        """prints the list sorted(ascending) order"""

        new_list = sorted(self)
        print("{}".format(new_list))
