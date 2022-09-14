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

    @property
    def size(self):
        """Get the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size
        Args:
            value (int): Value to set
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def my_print(self):
        """Print hashs in square form"""
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                for i in range(self.size):
                    print('{}'.format('#'), end='')
                print()
