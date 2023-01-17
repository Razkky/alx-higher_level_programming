#!/usr/bin/python3
"""Define a save to json file function"""
import json


def save_to_json_file(my_obj, filename):
    """ Save the json representation to a file
    Args:
        my_obj: python representation of the object
        filename: name of the file
        Return: JSON representation of the object
    """
    with open(filename, "w", encoding="utf-8") as filename:
        json_object = json.dump(my_obj, filename)
        return json_object
