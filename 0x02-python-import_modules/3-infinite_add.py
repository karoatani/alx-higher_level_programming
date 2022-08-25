#!/usr/bin/python3
import sys
sumation = 0
for i in sys.argv[1:]:
    sumation += int(i)
if __name__ == '__main__':
    print(sumation)
