#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_nums = []
    for i in matrix:
        new_list = [x ** 2 for x in i]
        new_nums.append(new_list)
    return new_nums
