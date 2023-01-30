#!/usr/bin/python3
"""This module has a function that divides value of
    list by a div"""

def matrix_divided(matrix, div):
    """This fucntions divides a matrix by div
        Args:
            matrix(list of int or float): matrix to be divided
            div(int, float): number to divide matrix by
        Return:
            new matrix 
            """
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    count = 0
    length = 0
    new_matrix = []
    for new in matrix:
        temp = []
        if count == 0:
            length = len(new)
            count += 1
        if length != len(new):
            raise TypeError("Each row of the matrix must have the same size")
        for value in new:
            if type(value) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            value = round(value/div, 2)
            temp.append(value)
        new_matrix.append(temp)
    return new_matrix

