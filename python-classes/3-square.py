#!/usr/bin/python3
"""Create the class 'Square'"""


class Square:
    """define the Square class"""
    def __init__(self, size=0):
        """initialisates the size of Square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """defines the area of Square"""
        area = self.__size ** 2
