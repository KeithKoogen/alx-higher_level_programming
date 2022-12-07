#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    dup_set = set()
    new_set = set()
    for i in set_1:
        for s in set_2:
            if i == s:
                dup_set.add(i)
    for i in set_1:
        if i not in dup_set:
            new_set.add(i)
    for i in set_2:
        if i not in dup_set:
            new_set.add(i)
