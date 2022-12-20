#!/usr/bin/python3
def safe_print_division(a, b):
    c = None
    try:
        c = a / b
    except:
        c = None
    finally:
        print("Inside result: {:f}".format(c))
