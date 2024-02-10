#!/usr/bin/python3
"""Function to check if an object is
   an instance of an specified class"""


def is_same_class(obj, a_class):
    """Return True if obj is an instance of a_class
	   otherwise False.
	"""
    if type(obj) == a_class:
        return (True)
    else:
        return (False)
