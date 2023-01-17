#!/usr/bin/python3
"""Define a read_file function"""


def read_file(filename=""):
    """A fucntion that reads a file
    Args:
        filename: name of the file
        """
    with open(filename, encoding="UTF8") as my_file:
        files = my_file.read()
        print(files, end="")
