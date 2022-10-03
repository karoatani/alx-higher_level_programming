#!/usr/bin/python3

from models.base import Base
""" Defines a Rectangle Class"""


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int): x of the rectangle
            y (int): y of the rectangle
            id (int): unique id
        Returns:
        None
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method"""
        self.setter_validation("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method"""
        self.setter_validation("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter method"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter method"""
        self.setter_validation("height", value)
        self.__x = value

    @property
    def y(self):
        """Getter method"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter method"""
        self.setter_validation('y', value)
        self.__y = value

    @staticmethod
    def setter_validation(attribute, value):
        """Validation for setter methods
        Args:
            attribute (str): attribute of the rectangle
            value (int): value to be set  
        Returns:
        None
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(attribute))
        if attribute == "x" or attribute == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(attribute))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(attribute))

    def area(self):
        """calculates the area"""
        return self.width * self.height

    def display(self):
        """Display the rectangle"""
        rectangle = ""
        print("\n" * self.y, end="")
        for i in range(self.height):
            rectangle += (" " * self.x) + ("#" * self.width) + "\n"
        print(rectangle, end="")

    def __str__(self):
        """Sring representation of object"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """Update the object"""
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """Return a dictionary of all attributes and their value"""
        return {'x': getattr(self, "x"),
                'y': getattr(self, "y"),
                'id': getattr(self, "id"),
                'height': getattr(self, "height"),
                'width': getattr(self, "width")}
