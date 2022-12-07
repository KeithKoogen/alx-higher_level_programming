#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set()
    sum = 0
    for i in range(len(my_list)):
        my_set.add(my_list[i])
    for s in my_set:
        sum += s
    return sum
