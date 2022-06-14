#!/usr/bin/python3
"""
Mudule: rectangle.py
Unittest: tests/test_rectangle.py
"""

from models.base import Base


class Rectangle(Base):
    """Returns the width attributes"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    """ATTRIBUTE GETTERS""""
    @property
    def width(self):
        """Returns the width attribute"""
        return self.__width

    @property
    def height(self):
        """Returns the height attribute"""
        return self.__height

    @property
    def x(self):
        """Returns the x attribute"""
        return self.__x

    @property
    def y(self):
        """Returns the y attribute"""
        return self.__y

    """ATTRIBUTE SETTERS""""
    @width.setter
    def width(self, value):
        """Sets the width attributes."""
        self.int_val("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height attributes."""
        self.int_val("height", value)
        self.__height = value

    @x.setter
    def x(self, value):
        """Sets the x attributes."""
        self.int_val("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        """Sets the y attributes."""
        self.int_val("y", value)
        self.__y = value
