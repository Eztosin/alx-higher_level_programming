#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        in_reverse = my_list[::-1]
        for i in in_reverse:
            print("{:d}".format(i))
        else:
            return None
