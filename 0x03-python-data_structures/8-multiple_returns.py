#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length > 0:
        new_tuple = (sentence[0], length)
    else:
        new_tuple = (None, 0)
