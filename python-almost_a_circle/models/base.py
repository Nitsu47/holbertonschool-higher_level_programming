#!/usr/bin/python3
"""Creates the Base model to start future classes"""
import json


class Base:
    """Base class to inheritance in future classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializates the object id"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)
