#!/usr/bin/python3
"""
Module: 6-rectangle.py
"""


class Rectangle:
    """ Defines a Rectangle class """

    # Public
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Retrieves the width of a Rectangle instance """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """ Returns a string representation of a Rectangle
        instance, filled with the '#' character """
        str_print = ""

        if self.__width == 0 or self.__height == 0:
            return str_print
        h = 1
        while h <= self.__height:
            str_print += "#" * self.__width
            if h < self.__height:
                str_print += "\n"
            h += 1
        return str_print

    def __repr__(self):
        """ Return a string representation of a Rectangle instance """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ Deletes a Rectangle instance and count """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
