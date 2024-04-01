#!/usr/bin/python3
"""Module Class to json"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure"""
    return obj.__dict__
