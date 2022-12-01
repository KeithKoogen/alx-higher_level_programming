#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    arguments = len(argv)
    if arguments > 2:
        print(f"{arguments - 1} arguments:")
        for i in range(1, arguments):
            print(f"{i}: {argv[i]}")

    if arguments == 2:
        print(f"{arguments - 1} argument:")
        print(f"1: {argv[1])

    if arguments < 2:
        print(f"0 arguments.")
