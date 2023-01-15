#!/usr/bin/python3
"""Define an instance checking function"""


def inherits_from(obj, a_class):
    """ Check if obj is instance of a class that inherited directly
    or indirectly from a specified class
    Args:
        obj: object to compare
        a_class: class to compare
    Return:
        True or False if otherwise"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
