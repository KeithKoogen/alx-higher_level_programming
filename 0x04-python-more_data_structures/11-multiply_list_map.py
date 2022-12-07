#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new_map = map(lambda x: x * x, my_list)
    new_list = list(new_map)
    return new_list
