#!/usr/bin/python3
""" Define to_json_string function"""
import json


def to_json_string(my_obj):
    """Get the JSON represention of an object
    Args:
        my_obj: python representation of the object
        Return: JSON representation of the object
    """
    json_object = json.dumps(my_obj)
    return json_object
