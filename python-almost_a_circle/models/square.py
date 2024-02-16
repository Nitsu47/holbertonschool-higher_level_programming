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
