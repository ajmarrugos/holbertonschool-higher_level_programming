#!/usr/bin/python3
"""
6. Improve Geometry
"""


class BaseGeometry():
    """
    Write a class BaseGeometry (based on 6-base_geometry.py).
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
