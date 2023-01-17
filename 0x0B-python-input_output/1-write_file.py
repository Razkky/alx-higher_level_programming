#!/usr/bin/python3
""" Define a fucntion that write to a file"""


def write_file(filename="", text=""):
    """Write to a file
    Args:
        filename: name of the file
        text: content of the file
        Return: Number of characters writing
    """
    with open(filename, "w", encoding="utf-8") as my_file:
        return my_file.write(text)
