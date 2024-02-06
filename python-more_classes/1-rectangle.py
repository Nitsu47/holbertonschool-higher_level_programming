#!/usr/bin/python3
"""Creates a 'Rectangle' class."""


class Rectangle:
    """defines the Rectangle class"""
    def __init__(self, width=0, height=0):
        """initializates the rectangle dimensions"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """returns the Rectangle's width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the Rectanle`s width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns the Rectangle`s height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the Rectanle`s height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
