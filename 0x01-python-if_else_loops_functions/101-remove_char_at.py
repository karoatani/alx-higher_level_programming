#!/usr/bin/python3
def remove_char_at(str, n):
    cpy = [i for i in str]
    cpy[n] = ''
    return ''.join(cpy)
