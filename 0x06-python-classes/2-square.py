#!/usr/bin/python3
#!/usr/bin/python3
""" Define a class Square """


class Square:
    """A square class model"""

    def __init__(self, size=0):
        """Initialized a square
        Args:
            size (:obj:`int`, optional): size of the square
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
