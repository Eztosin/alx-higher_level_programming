#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    empty_index = my_list.copy()
    if idx >= len(my_list) or idx < 0:
        return empty_index
    empty_index = my_list[:idx] + my_list[idx+1:]
    return empty_index
