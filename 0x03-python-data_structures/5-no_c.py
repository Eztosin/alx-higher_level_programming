#!/usr/bin/python3
def no_c(my_string):
    rm_c = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            rm_c += char
    return rm_c
