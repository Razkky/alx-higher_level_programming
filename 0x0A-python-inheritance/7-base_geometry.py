#!/usr/bin/python3
""" Define a class BaseGeometry"""


class BaseGeometry:
    """Represent a  BaseGeometry class"""

    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A fucntion that validate value
        Args:
            name: name of parameter
            value: value to validate
        Raise:
            TypeError: if value is not an integer
            ValueError: if value <= 0
            """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
