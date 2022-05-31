#!/usr/bin/python3
"""
Module: 2-rectangle.py
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
        """Retrieves the height of a Rectangle instance """
        return self.__height

    @width.setter
    def width(self, value):
        """ Retrieves the width of a Rectangle instance """
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """ Retrieves the height of a Rectangle instance """
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """ Returns area of rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns perimeter of rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
