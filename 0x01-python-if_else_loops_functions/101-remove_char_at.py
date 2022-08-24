#!/usr/bin/python3
def remove_char_at(str, n):
    cpy = [i for i in str]
    try:
        cpy[n] = ''
    except IndexError:
        return str
    return ''.join(cpy)
