#!/usr/bin/python3
"""checks if the object is an instance of a class that
   inherited (directly or indirectly) from the specified class"""


def inherits_from(obj, a_class):
    """Returns True if obj is inhereted, otherwhise False."""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return (True)
    else:
        return (False)
