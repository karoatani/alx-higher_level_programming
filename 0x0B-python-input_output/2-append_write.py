#!/usr/bin/python3
def append_write(filename="", text=""):
    with open(filename, 'a') as fd:
        return fd.write(text)
