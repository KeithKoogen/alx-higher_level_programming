#!/usr/bin/python3
def uppercase(str):

    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            i = i - 32
            print("{%c}".format(i), end='')
        else:
            print("{%c}".format(i), end='')
