#!/usr/bin/python3
"""Define a funciton that returns True if the object is an
    instance or is an instance of a subclass or False if
    otherwise"""


def is_kind_of_class(obj, a_class):
    """ Check if obj is an instance of a_class or is a subclass of a_class
    Args:
        obj: object to compare
        a_class: class to compare
    Return:
        True or False if otherwise"""
    return isinstance(obj, a_class)
