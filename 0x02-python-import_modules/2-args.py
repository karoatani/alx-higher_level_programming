#!/usr/bin/python3
import sys
length = len(sys.argv)
if length == 1:
    print('0 arguments.')
else:
    print('{} arguments:'.format(length - 1))
    for index, i in enumerate(sys.argv[1:], 1):
        print('{}: {}'.format(index, i))
