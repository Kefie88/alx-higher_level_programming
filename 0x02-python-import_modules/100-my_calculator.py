#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":
    length = len(argv)
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if length == 4:
        op = argv[2]
        a = int(argv[1])
        b = int(argv[3])
    if op == '+':
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, add(a, b)))
    elif op == '-':
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, sub(a, b)))
    elif op == '*':
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, mul(a, b)))
    elif op == '/':
         print("{:d} {:s} {:d} = {:d}".format(a, op, b, div(a, b)))
    else:
         print("Unknown operator. Available operators: +, -, * and /")
         exit(1)
