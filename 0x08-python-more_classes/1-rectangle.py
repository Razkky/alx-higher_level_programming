#!/usr/bin/python3
""" Define a rectangle"""


class Rectangle:
    """Represent a rectangle"""

    def __init__(self, width, height):
        """Initialize private instance"""

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieve value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be and integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieve the height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of a rectangle"""
        if not isinstance(value, int):
            raise TypeError("height  must be and integer")
        elif value < 0:
            raise ValueError("height  must be >= 0")
        else:
            self.__height = value
