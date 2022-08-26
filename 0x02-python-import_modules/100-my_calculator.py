#!/usr/bin/python3
from calculator_1 import add, sub, div, mul
import sys
if __name__ == '__main__':
    if len(sys.argv[1:]) != 3:
        print('{}'.format('Usage: ./100-my_calculator.py <a> <operator> <b>'))
        sys.exit(1)
    operator = sys.argv[2]
    if operator == '+':
        print('{} + {} = {}'.format(sys.argv[1],sys.argv[3],add(int(sys.argv[1]),int(sys.argv[3]))))
    elif operator == '-':
        print('{} - {} = {}'.format(sys.argv[1],sys.argv[3],sub(int(sys.argv[1]),int(sys.argv[3]))))
    elif operator == '*':
        print('{} * {} = {}'.format(sys.argv[1],sys.argv[3],mul(int(sys.argv[1]),int(sys.argv[3]))))
    elif operator == '/':
        print('{} / {} = {}'.format(sys.argv[1],sys.argv[3],div(int(sys.argv[1]),int(sys.argv[3]))))
    else:
        print('{}'.format('Unknown operator. Available operators: +, -, * and /'))
        sys.exit(1)
