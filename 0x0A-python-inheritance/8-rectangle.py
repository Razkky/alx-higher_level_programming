#!/usr/bin/python3
"""Define a class Rectangle that inherit class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Define a rectangle"""

    def __init__(self, width, height):
        """ Initialize a rectangle
        Args:
            width: width of rectangle
            height: height of rectangle
            """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
