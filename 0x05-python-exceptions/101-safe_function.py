#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        answer = fct(*args)
        return answer
    except (IndexError, ValueError, TypeError, ZeroDivisionError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return None
