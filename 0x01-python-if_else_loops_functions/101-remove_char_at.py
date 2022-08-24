#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    cpy = [i for i in str]
    try:
        cpy[n] = ''
    except IndexError:
        return str
    return ''.join(cpy)
