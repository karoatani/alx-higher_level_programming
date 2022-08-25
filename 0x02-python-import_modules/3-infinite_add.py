#!/usr/bin/python3
import sys
sumation = 0
for i in sys.argv[1:]:
    sumation += int(i)
print(sumation)
