#!/usr/bin/python3

from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        """Initialization
        Args:
            width (int): width of the square
            height (int): height of the square
            size (int): square size
            x (int): x of the square
            y (int): y of the square
            id (int): unique id
        Returns:
        None
        """

    def __str__(self):
        """Object Represntation"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """Getter method"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the object"""
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def to_dictionary(self):
        """Return a dictionary of all attributes and their value"""
        return {'x': getattr(self, "x"),
                'y': getattr(self, "y"),
                'id': getattr(self, "id"),
                'size': getattr(self, "size")}
