#!/usr/bin/python3
"""Creates a 'Rectangle' class."""


class Rectangle:
    """defines the Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializates the rectangle dimensions"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """defines the area of Rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """defines the perimeter of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__height * 2 + self.__width * 2

    def __str__(self):
        """defines the str method to print Rectangle representation"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        return ((str(self.print_symbol) * self.__width + "\n")
                * (self.__height - 1) + str(self.print_symbol) * self.__width)

    def __repr__(self):
        """defines the repr method for a representation of Rectangle"""
        return ("Rectangle(" + str(self.__width) + ", " + str(self.__height)
                + ")")

    def __del__(self):
        """deletes an instance of Rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        if rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns new instance of Rectangle as Square"""
        return cls(size, size)
