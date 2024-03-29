#!/usr/bin/python3
"""Define add_integer function
    Take two intgers 
    Int a
    int b
    return sum"""

def add_integer(a, b=98):
    """ Adds two integers
    Return:
        sum"""
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
