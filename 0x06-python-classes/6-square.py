#!/usr/bin/python3
""" Define a square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize instance attribute

        Args:
            size: size of square
            position: position of the new square
            """
        self.__size = size
        self.__position = position
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

    @property
    def position(self):
        """Get the position of the square"""
        return self.__position

    @position.setter
    def position(self, position):
        """Set value for position of square"""
        if not isinstance(position, tuple) or len(position) != 2 or not all(isinstance(num, int) for num in position) or not all(num >0 for num in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position
    def area(self):
        """ Get area of square"""
        return self.__size * self.__size

    def my_print(self):
        """print square with character # to stdout"""
        if self.__size == 0:
            print()
        else:
            [print("") for i in range(self.__position[1])]
            for i in range(self.__size):
                [print("", end="") for j in range(self.__position[0])]
                [print("#",end="") for k in range(self.__size)]
                print()
