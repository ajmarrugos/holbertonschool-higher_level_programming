#!/usr/bin/python3
"""
Private instance attribute: size:
    - property def size(self)
    - property setter def size(self, value)
Private instance attribute: position:
    - property def position(self)
    - property setter def position(self, value)
Instantiation with optional size and optional position.
Public instance method: def area(self).
Public instance method: def my_print(self).
"""


class Square:
    """Represents an empty square"""
    def __init__(self, size=0, position=(0, 0)):
        """ inizialize Square class """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size

        if type(position) != tuple or \
           not all(type(x) == int for x in position) or \
           not all(x >= 0 for x in position) or \
           len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self._Square__position = position

    def area(self):
        """Method function to return the 'area' of the Square"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """Method to return value stored in the private variable 'size'"""
        return self.__size

    @property
    def position(self):
        """Method to return value stored in the private variable 'position'"""
        return self.__position

    @size.setter
    def size(self, value):
        """Method which sets a new value to the 'size' instace/attribute"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """Sets the position to a value."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Method that draws a square with '#' to the Stdout"""
        [print() for x in range(self.position[1])]
        print("\n".join(["".join(([" "] * self.position[0]) +
                                 ["#" for x in range(self.size)])
                         for y in range(self.size)]))


