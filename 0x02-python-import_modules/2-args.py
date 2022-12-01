#!/usr/bin/python3
from sys import argv
arguments = len(argv)
if __name__ == '__main__':
    if arguments > 2:
        print("{:d} arguments:".format(arguments - 1))
        for i in range(1, arguments):
            print("{:d}: {:s}".format(i, argv[i]))
    if arguments == 2:
        print("1 argument:")
        print("1: {:s}".format(argv[1]))
    if arguments < 2:
        print(f"0 arguments.")
