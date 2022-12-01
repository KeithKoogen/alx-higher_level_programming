#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    arguments = len(argv)

    if arguments == 2:
        print("1 argument:")
        print("1: {:s}".format(argv[1]))
    elif arguments > 2:
        print("{:d} arguments:".format(arguments - 1))
        for i in range(1, arguments):
            print("{:d}: {:s}".format(i, argv[i]))
    else:
        print(f"0 arguments.")
