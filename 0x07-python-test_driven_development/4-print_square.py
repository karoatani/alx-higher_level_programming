#!/usr/bin/python3
"""Defines a function to print """


def print_square(size):
    """ Prints a Square 
    Args:
    size (str): value

    Raises:
        TypeError: if arguments are not integer typeerror is raised
                    and if size < 0 raises TypeError
                    and if size is an instance of float and size is less than 0
                    raises TypeError   
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')

    for _ in range(4):
        for _ in range(4):
            print('#', end='')
        print()
