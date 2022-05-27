#!/usr/bin/python3
"""
add_integer:
    - Checks if parameters are bool
    - Checks if parameters are int or float
    - Casts the parameters from float to int
    - Returns sum of parameters
"""


def add_integer(a, b=98):
    """
    Return sum of a and b.
    """

    if isinstance(a, bool):
        raise TypeError("a must be an integer")
    if isinstance(b, bool):
        raise TypeError("b must be an integer")

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)

    return (a + b)
