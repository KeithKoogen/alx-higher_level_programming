#!/usr/bin/python3
def uppercase(str):

    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            ch = ord(i) - 32
        else:
            ch = ord(i)
        print("{:c}".format(ch), end='')
        
    print("")
           
