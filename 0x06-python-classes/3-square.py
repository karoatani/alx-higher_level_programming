#!/usr/bin/python3
""" Define a class Square """


class Square:
    """A square class model"""

    def __init__(self, size=0):
        """Initialized a square
        Args:
            size (int): size of the square.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Calculate the area"""
        return self.__size * self.__size
