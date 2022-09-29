#!/usr/bin/python3
def read_file(filename=""):
    with open(filename) as fd:
        data = fd.read()
    print(data)
