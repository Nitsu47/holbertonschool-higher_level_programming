#!/usr/bin/python3
"""Creates a new empty 'BaseGeometry' class"""


class BaseGeometry:
    """empty class"""
    pass

    def area(self):
        """Raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value, raise exceptions if value is not int"""
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
