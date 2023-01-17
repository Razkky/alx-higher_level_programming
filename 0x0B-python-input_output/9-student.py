#!/usr/bin/python3
""" Define a student class"""


class Student:
    """ A student class that defines a student"""

    def __init__(self, first_name="None", last_name="None", age=0):
        """Initialize the student class
        Args:
            first_name(str): first name of the student
            last_name(str): last name of the student
            age: age of the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return dict representaion of a student object"""
        return self.__dict__
