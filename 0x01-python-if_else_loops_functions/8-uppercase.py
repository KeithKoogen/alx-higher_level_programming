#!/usr/bin/python3
def uppercase(str):

    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            ch = ord(i) - 32
            print("{:c}".format(ch), end='')
        else:
            print("{:c}".format(ord(i)), end='')
