#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key:
        del_key = del a_dictionary[key]
        return del_key
    return a_dictionary
