#!/usr/bin/python3
"""Defines function to add integers"""


def add_integer(a, b=98):
    """ adds two integer together
    Args:
    a (int): integer or float
    b (int): integer or float
    Raises:
        TypeError: if arguments are not either int or float typeerror is raised 
    """
    if not isinstance(a, int) and isinstance(a, float):
        raise TypeError('a must be an integer')
    if not isinstance(b, int) and isinstance(b, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
