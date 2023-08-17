#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for i in sorted(a_dictionary.keys()):
        if key:
            a_dictionary[i] = value
        else:
            a_dictionary[i] = key
    return a_dictionary
