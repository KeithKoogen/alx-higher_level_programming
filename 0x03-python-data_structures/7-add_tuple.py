#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2:
        if len(tuple_b) >= 2:
            a = (tuple_a[0] + tuple_b[0])
            b = tuple_a[1] + tuple_b[1]
    new_tuple = (a, b)
    return new_tuple
