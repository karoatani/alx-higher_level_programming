#!/usr/bin/python3
""" Define a class Square """


class Square:
    """A square class model"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialized a square
        Args:
            size (int): size of the square.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
        self.__position = position

    def area(self):
        """Calculate the area"""
        return self.__size * self.__size

    @property
    def size(self):
        """Get the size"""
        return self.__size

    @property
    def position(self):
        """Get the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """set a position
        Args:
            value (tuple): a tuple.
        """
        if isinstance(value, tuple):
            for i in value:
                if isinstance(i, int):
                    continue
                raise TypeError(
                    'position must be a tuple of 2 positive integers')
            self.__position = value
        else:
            raise TypeError(
                'position must be a tuple of 2 positive integers')

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
            for _ in range(0, self.size):
                if not self.__position[1] > 0:
                    print('{}'.format(self.__position[0] * ' '), end='')
                for _ in range(0, self.size):
                    print('{}'.format('#'), end='')
                print()
