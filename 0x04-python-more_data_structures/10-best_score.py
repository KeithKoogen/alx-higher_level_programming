#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary.values()) > 0:
        best = max(a_dictionary, key=a_dictionary.get)
        return best
    else:
        return None
