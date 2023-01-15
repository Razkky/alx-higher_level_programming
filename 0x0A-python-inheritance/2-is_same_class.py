#!/usr/bin/python3
""" Define a function that returns true if an
    object is an isntance of a classs"""


def is_same_class(obj, a_class):
    """check if obj is exactly an instance of a_class
    Args:
        obj: the object
        a_class: the class to match with

    Return:
        true if obj is an instance of a_class"""
    if type(obj) == a_class:
        return True
    return False
