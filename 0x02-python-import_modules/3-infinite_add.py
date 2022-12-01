#!/usr/bin/python3
def add_args(argv):
    count = 0
    if len(argv) > 1:
        for i in range(1, len(argv)):
            count += int(argv[i])
    return count


if __name__ == '__main__':
    from sys import argv
    sum = add_args(argv)
    print(sum)
