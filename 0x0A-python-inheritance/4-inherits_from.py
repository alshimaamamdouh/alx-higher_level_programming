#!/usr/bin/python3
"""
task 4
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.
    """
    return issubclass(type(obj), a_class)
