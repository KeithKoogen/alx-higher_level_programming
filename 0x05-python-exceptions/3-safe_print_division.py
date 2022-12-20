#!/usr/bin/python3
def safe_print_division(a, b):
    c = None
    try:
        c = a / b
    except ZeroDivisionError:
        c = None
    finally:
        if c is None:
            print("Inside result: None")
            return None
        else:
            print("Inside result: {0:.1f}".format(c))
            return c
