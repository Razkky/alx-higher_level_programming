#!/usr/bin/python3
"""Define a class_to_json Python class"""


def class_to_json(obj):
    """Return a dictionary representaion of the obj attrributes"""
    return obj.__dict__
