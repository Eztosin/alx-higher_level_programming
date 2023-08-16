#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    not_in = set()
    for i in set_1:
        if i not in set_2:
            not_in.add(i)
    for i in set_2:
        if i not in set_1:
            not_in.add(i)
    return not_in
