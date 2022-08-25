#!/usr/bin/python3
import sys
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('{}'.format('0 arguments.'))
    else:
        print('{} arguments:'.format(len(sys.argv) - 1))
        for index, i in enumerate(sys.argv[1:], 1):
            print('{}: {}'.format(index, i))
