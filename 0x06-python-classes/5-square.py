#!/usr/bin/python3
""" Define a square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize instance attribute

        Args:
            size: size of square
            """
        self.__size = size

    @property
    def size(self):
        """Get the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """ Set the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must b >= 0")
        else:
            self.__size = value

    def area(self):
        """ Get area of square"""
        return self.__size * self.__size

    def my_print(self):
        """print square with character # to stdout"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for x in range(self.__size):
                    print("#", end="")
                print()
