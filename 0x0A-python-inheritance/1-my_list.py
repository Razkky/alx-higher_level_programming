#!/usr/bin/python3
""" Defines a class that prints a list in ascending order"""


class MyList(list):
    """sub class of the super class list"""
    def __init__(self):
        """Initialze the object"""
        super().__init__()

    def print_sorted(self):
        """prints list in sorted order"""
        print(sorted(self))
