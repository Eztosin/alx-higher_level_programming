#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) < ord('a') and ord(i) < ord('z'):
            print("{}".format(i), end='')
        else:
            i = chr(ord(i) - 32)
            print("{}".format(i), end='')
