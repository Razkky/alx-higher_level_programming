#!/usr/bin/python3
def max_integer(my_list=[]):
    maximum = 0
    if my_list:
        for num in my_list:
            if num > maximum:
                maximum = num
            else:
                continue
        return maximum
    return None
