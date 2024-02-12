#!/usr/bin/python3
"""Creates a Rectangle class that inherites from the BaseGeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Creates a rectangle, width and height """
    def __init__(self, width, height):
        """Initializates the Rectangle dimensions"""
        self.__width = width
        super().integer_validator("width", width)
        self.__height = height
        super().integer_validator("height", height)
