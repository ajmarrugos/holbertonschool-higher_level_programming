#!/usr/bin/python3
"""
Module: 0-add_integer.py
Doctest: 0-add_integer.txt
"""


def add_integer(a, b=98):
    """ Recives 2 parameters and one is already defined"""

    """ Checks if parameters are bool """
    if isinstance(a, bool):
        raise TypeError("a must be an integer")
    if isinstance(b, bool):
        raise TypeError("b must be an integer")

    """ Checks if parameters are int or float """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    """ Casts the parameters from float to int """
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)

    """ Returns sum of parameters """
    return (a + b)
