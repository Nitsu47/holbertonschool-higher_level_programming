#!/usr/bin/python3
"""Checks if an object is an insit ance of a class or
   inhereted from a class
"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of a_class or
       is an instance of a class that inherited from a_class
       otherwise return False
    """

    if type(obj) == a_class or isinstance(obj, a_class):
        return (True)
    else:
        return (False)
