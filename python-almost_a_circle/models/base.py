#!/usr/bin/python3
"""Creates the Base model to start future clases"""


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializates the object id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
