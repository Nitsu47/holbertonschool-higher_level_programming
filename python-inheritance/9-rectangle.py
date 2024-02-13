#!/usr/bin/python3
"""Creates a Rectangle class that inherites from the BaseGeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Creates a rectangle, width and height """
    def __init__(self, width, height):
        """Initializates the Rectangle dimensions"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns the string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
