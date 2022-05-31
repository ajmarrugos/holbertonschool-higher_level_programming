#!/usr/bin/python3
"""
Module: 0-rectangle.py
"""


class Rectangle:
    """ Defines a Rectangle class """

    def __init__(self, width=0, height=0):
        """ Retrieves the width of a Rectangle instance """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ Retrieves the width of a Rectangle instance """
        return self.__width

    @property
    def height(self):
        """Retrieves the height of a Rectangle instance."""
        return self.__height

    @width.setter
    def width(self, value):
        """ Retrieves the width of a Rectangle instance """
        if type(width) is not int:
            raise TypeError("width must be an integer")

        if width < 0:
            raise ValueError("width must be >= 0")

    @height.setter
    def height(self, value):
        if type(height) is not int:
            raise TypeError("height must be an integer")

        if height < 0:
            raise ValueError("height must be >= 0")
