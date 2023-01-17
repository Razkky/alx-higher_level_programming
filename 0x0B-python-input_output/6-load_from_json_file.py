#!/usr/bin/python3
"""Create an object from json file"""
import json


def load_from_json_file(filename):
    """Creates a python object from a json file
    Args:
        filename: name of file
    """
    with open(filename, encoding="utf-8") as f:
        my_file = f.read()
        my_file = json.loads(my_file)
        return my_file
