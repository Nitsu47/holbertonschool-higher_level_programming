#!/usr/bin/python3
"""Creation and definition of Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class, inhereted from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """inits Rectangle attributes"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """returns width value of Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width value for Rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """returns height value of Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height value for Rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """returns x value(x axis) of Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the x value(x axis) for Rectangle"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """returns y value(y axis) of Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the y value(y axis) for Rectangle"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
