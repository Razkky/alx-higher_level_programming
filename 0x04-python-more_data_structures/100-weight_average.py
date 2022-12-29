#!/usr/bin/python3
def weight_average(my_list=[]):
    weight = 0
    numerator = 0
    for x, y in my_list:
        numerator += x * y
        weight += y
    return (numerator / weight)
