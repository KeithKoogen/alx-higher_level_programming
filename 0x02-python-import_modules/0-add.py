#!/usr/bin/python3

if __name__ == '__main__':
    from add_0 import add
    a = 1
    b = 2
    total = add(a, b)
    print("{num1} + {num2} = {sum1}".format(num1=a, num2=b, sum1=total))
