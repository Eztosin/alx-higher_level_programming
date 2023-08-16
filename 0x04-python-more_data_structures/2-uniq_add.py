#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_nums = set()
    result = 0
    for i in my_list:
        if i not in unique_nums:
            result = result + i
            unique_nums.add(i)
    return result
