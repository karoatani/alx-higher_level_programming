#!/usr/bin/python3
def add_integer(a, b=98):
    """ adds two integer together
    Args:
    a (int): integer or float
    b (int): integer or float
    """
    if not isinstance(a, int) or isinstance(a, float):
        raise TypeError('a must be an integer')
    if not isinstance(b, int) or isinstance(b, float):
        raise TypeError('b must be an integer')
    a = int(a)
    b = int(b)
    return a + b
