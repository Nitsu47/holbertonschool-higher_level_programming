#!/usr/bin/python3
"""Creation and definition of Square class that inherits Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a square, inherits Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """inits square x and y axis, the size and id of a square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """defines the str method to print Square with his attributes"""
        return ("[Square] ({}) {}/{} - {}".format
                (self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """returns the size of square using width and height"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the square size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assing arguments to attributes of Square"""
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.size = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 4:
            self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y
        }
