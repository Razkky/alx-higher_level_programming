#!/usr/bin/python3
""" Define json to python function"""
import json


def from_json_string(my_str):
    """ Get the python object representation from a Json string
    Args:
        my_obj: python representation of the object
        Return: JSON representation of the object
    """
    return json.loads(my_str)
