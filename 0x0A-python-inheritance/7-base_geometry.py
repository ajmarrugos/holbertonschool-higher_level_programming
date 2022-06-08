#!/usr/bin/python3
"""
7-base_geometry.py
"""


class BaseGeometry():
    """ Class for BaseGeometry """

    def area(self):
        """ Causes exception when called """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates value """
        if isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
