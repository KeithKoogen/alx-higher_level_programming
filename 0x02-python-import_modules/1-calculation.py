#!/usr/bin/python3

if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    totalsum = add(a, b)
    totalsub = sub(a, b)
    totalmul = mul(a, b)
    totaldiv = div(a, b)
    print("{num1} + {num2} = {sum1}".format(num1=a, num2=b, sum1=totalsum))
    print("{num1} - {num2} = {sum1}".format(num1=a, num2=b, sum1=totalsub))
    print("{num1} * {num2} = {sum1}".format(num1=a, num2=b, sum1=totalmul))
    print("{num1} / {num2} = {sum1}".format(num1=a, num2=b, sum1=totaldiv))
