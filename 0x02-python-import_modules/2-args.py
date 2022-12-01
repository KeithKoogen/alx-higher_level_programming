#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    arguments = len(argv)
    if arguments > 2:
        print(f"{arguments - 1} arguments:")
        for i in range(1, arguments):
            print("{num}: {arg}".format(num=i, arg=argv[i]))

    if arguments == 2:
        print("1 argument:")
        print("1: {arg}".format(arg=argv[1]))

    if arguments < 2:
        print(f"0 arguments.")
