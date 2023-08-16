#!/usr/bin/python3
def common_elements(set_1, set_2):
    init = set()
    for i in set_1:
        for j in set_2:
            if i == j:
                init.add(i)
    return init
