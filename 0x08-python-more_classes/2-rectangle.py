#!/usr/bin/python3
"""
Defines an  rectangle class
"""


class Rectangle:
    """
    Creates an rectangle class.
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Returns the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    """Calculates the area"""

    def area(self):
        return self.width * self.height

    """Calculates the perimeter"""

    def perimeter(self):
        return 2 * (self.width + self.height)
