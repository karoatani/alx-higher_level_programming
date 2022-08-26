#!/usr/bin/python3
from ast import arguments
from calculator_1 import add, sub, div, mul
import sys
if __name__ == '__main__':
    if len(sys.argv[1:]) != 3:
        print('{}'.format('Usage: ./100-my_calculator.py <a> <operator> <b>'))
        sys.exit(1)
    operator = sys.argv[2]
    arguments_1 = sys.argv[1]
    arguments_2 = sys.argv[3]
    if operator == '+':
        print('{} + {} = {}'.format(
            arguments_1, arguments_2, add(int(arguments_1), int(arguments_2))))
    elif operator == '-':
        print('{} - {} = {}'.format(
            arguments_1, arguments_2, sub(int(arguments_1), int(arguments_2))))
    elif operator == '*':
        print('{} * {} = {}'.format(
            arguments_1, arguments_2, mul(int(arguments_1), int(arguments_2))))
    elif operator == '/':
        print('{} / {} = {}'.format(
            arguments_1, arguments_2, div(int(arguments_1), int(arguments_2))))
    else:
        print('{}'.format(
            'Unknown operator. Available operators: +, -, * and /'))
        sys.exit(1)
