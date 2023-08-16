#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        result_1 = tuple_a[0] + tuple_b[0]
        result_2 = tuple_a[1] + tuple_b[1]
        return (result_1, result_2)
    elif len(tuple_a) >= 2 and len(tuple_b) >= 1:
        result_1 = tuple_a[0] + tuple_b[0]
        result_2 = tuple_a[1]
        return (result_1, result_2)
    elif len(tuple_a) >= 2 and len(tuple_b) >= 0:
        result_1 = tuple_a[0]
        result_2 = tuple_a[1]
        return (result_1, result_2)
    else:
        return None
