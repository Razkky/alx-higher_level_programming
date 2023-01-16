#!/usr/bin/python3
"""Define a class Rectangle"""
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


    def area(self):
        """Calculate area of a rectangle
        Return: Area
        """
        return self.__width * self.__height

    def __str__(self):
        """Return a string to print"""
        return "[{}] {}/{}".format(self.__class__.__name__, self.__width, self.__height)
