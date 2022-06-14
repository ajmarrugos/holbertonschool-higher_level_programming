#!/usr/bin/python3
"""
Mudule: rectangle.py
Unittest: tests/test_rectangle.py
"""

from models.base import Base


class Rectangle(Base):
    """Initializes a Rectangle instance"""
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

    """CALCULATION METHODS"""
    def area(self):
        """Returns the area of rectangle"""
        return self.__width * self.__height

    """REPRESENTATION METHODS"""
    def display(self):
        """Prints a rectangle to stdout"""
        for offset_y in range(self.y):
            print("")
        for row in range(self.height):
            for offset_x in range(self.x):
                print("", end=" ")
            for col in range(self.width):
                print('#', end="")
            print("")

    def __str__(self):
        """Returns a string representation of a Rectangle"""

        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    """CLASS ATTRIBUTES UPDATER"""
    def update(self, *args, **kwargs):
        """Updates rectangle values"""
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                setattr(self, k, v)
        elif len(args) != 0:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass
        else:
            print()

    """DATA STRUCTURE METHODS"""
    def to_dictionary(self):
        """Returns the dictionary"""

        return {'x': self.__x, 'y': self.__y, 'id': self.id,
                'height': self.__height, 'width': self.__width}