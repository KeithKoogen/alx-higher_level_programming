#!/usr/bin/python3
def safe_print_division(a, b):
    c = None
    try:
        c = a / b
    except:
        c = None
    finally:
        if c == None:
            print("Inside result: None")
        else:
            print("Inside result: {0:.2f}".format(c))
