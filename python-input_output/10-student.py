#!/usr/bin/python3
"""Student class"""


class Student():
    """Student´s attributes"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        if not isinstance(attrs, list):
            return self.__dict__
        filter_data = {}
        for i in attrs:
            if i in self.__dict__:
                filter_data[i] = self.__dict__[i]
        return (filter_data)
