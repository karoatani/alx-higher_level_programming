#!/usr/bin/python3
from inspect import isclass


def is_same_class(obj, a_class):
    if type(obj) == a_class:
        return True
    return False
