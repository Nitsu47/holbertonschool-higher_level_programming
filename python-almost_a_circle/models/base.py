#!/usr/bin/python3
"""Creates the Base model to start future classes"""


class Base:
    """Base class to inheritance in future classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializates the object id"""
        if id is None:
            Base.__nb_objects += 1
            id = Base.__nb_objects
        else:
            self.id = id
