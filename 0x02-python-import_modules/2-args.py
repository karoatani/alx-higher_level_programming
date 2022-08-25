#!/usr/bin/python3
import sys
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('{}'.format('0 arguments.'))
    elif len(sys.argv) == 2:
        print('{} argument:'.format(len(sys.argv) - 1))
        print('{}: {}'.format(len(sys.argv) - 1, sys.argv[len(sys.argv) - 1]))
    else:
        print('{} arguments:'.format(len(sys.argv) - 1))
        for index, i in enumerate(sys.argv[1:], 1):
            print('{}: {}'.format(index, i))
