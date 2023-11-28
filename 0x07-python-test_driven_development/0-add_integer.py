#!/usr/bin/python3
""""
task 0
Alshimaa
module
"""


def add_integer(a, b=98):
    """
    add integer
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
