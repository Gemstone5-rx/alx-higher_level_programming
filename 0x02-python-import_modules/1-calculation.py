#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


if __name__ == "__main__":
    a = 10
    b = 5
    print("{a} + {b} = {add}".format(a=a, b=b, add=add(a, b)))
    print("{a} - {b} = {sub}".format(a=a, b=b, sub=sub(a, b)))
    print("{a} * {b} = {mul}".format(a=a, b=b, mul=mul(a, b)))
    print("{a} / {b} = {div}".format(a=a, b=b, div=div(a, b)))
