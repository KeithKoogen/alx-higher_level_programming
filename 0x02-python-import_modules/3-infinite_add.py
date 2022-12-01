#!/usr/bin/python3
def add_args(argv):
    count = 0;
    for i in range(len(argv)):
        count += arv[i];
    return count

if __name__ == '__main__':
    from sys import argv
    sum = add_args(argv)
    print(sum)
