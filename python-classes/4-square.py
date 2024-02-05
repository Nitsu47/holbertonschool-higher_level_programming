#!/usr/bin/python3
"""Create the class 'Square'"""


class Square:
    """define the Square class"""
    def __init__(self, size=0):
        """initialisates the size of Square"""
        self.__size = size

    def area(self):
        """defines the area of Square"""
        return self.__size ** 2

    @property
    def size(self):
        self.__size

    @size.setter
    def size(self, value)
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if value < 0:
        raise ValueError("size must be >= 0")
    self.__size = value
