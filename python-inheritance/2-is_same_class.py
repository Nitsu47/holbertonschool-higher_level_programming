#!/usr/bin/python3
"""Function to check instances in a class"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance, otherwise False"""

    if type(obj) == a_class:
        return True
    else:
        return False
