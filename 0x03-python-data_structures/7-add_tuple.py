#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result_1 = tuple_a[0] if len(tuple_a) >= 1 else 0
    result_2 = tuple_a[1] if len(tuple_a) >= 2 else 0

    result_1 += tuple_b[0] if len(tuple_b) >= 1 else 0
    result_2 += tuple_b[1] if len(tuple_b) >= 2 else 0

    if len(tuple_a) >= 2 or len(tuple_b) >= 1:
        return (result_1, result_2)
    elif len(tuple_a) == 0 and len(tuple_b) == 0:
        return 0
    else:
        return None
