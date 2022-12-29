#!/usr/bin/python3
def weight_average(my_list=[]):
    weight = 0
    numerator = 0
    if my_list:

        for x, y in my_list:
            numerator += x * y
            weight += y
        return (numerator / weight)
    else:
        return 0
