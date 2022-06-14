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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """ATTRIBUTE GETTERS"""
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

    """ATTRIBUTE VALIDATION METHOD"""
    def int_val(self, atts, value):
        """Validates entry data in attributes"""
        if type(value) is not int:
            raise TypeError(f"{atts} must be an integer")
        if atts == "width" or atts == "height":
            if value <= 0:
                raise ValueError(f"{atts} must be > 0")
        if atts == "x" or atts == "y":
            if value < 0:
                raise ValueError(f"{atts} must be >= 0")

    """ATTRIBUTE SETTERS"""
    @width.setter
    def width(self, value):
        """Sets the width attribute"""
        self.int_val("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height attribute"""
        self.int_val("height", value)
        self.__height = value

    @x.setter
    def x(self, value):
        """Sets the x attribute"""
        self.int_val("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        """Sets the y attribute"""
        self.int_val("y", value)
        self.__y = value

    def area(self):
        """Returns the area of rectangle"""
        return self.__width * self.__height