#!/usr/bin/python3
"""Create the class 'Square'"""


class Square:
    """define the Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """initialisates the size of Square"""
        self.__size = size
        self.__position = position

    def area(self):
        """defines the area of Square"""
        return self.__size ** 2

    def position(self):
        """defines the position of square"""
        return self.__position
        
    def my_print(self):
        """Prints the square"""
        if self.size == 0:
            print()
        else:
            position = self.position
            if position[1] > 0:
                for i in range(position[1]):
                    print()
            for i in range(self.size):
                print(" " * position[0] + "#" * self.size)

    @property
    def size(self):
        """returns the size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """returns the position of square"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the position of square"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
