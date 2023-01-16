#!/usr/bin/python3
""" Define a square class that inherit the rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class sqaure """
    def __init__(self, size):
        """Initialize a square
        Args:
            size: size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculate area of a square
        Return: Area of a square"""
        return self.__size * self.__size
