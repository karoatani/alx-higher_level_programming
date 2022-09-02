#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    return dict(filter(lambda v: value not in v, a_dictionary.items()))
