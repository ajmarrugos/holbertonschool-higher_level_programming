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
        """
        Init class with args: size
        runs a check to ensure size data is correct type and value.
        """
        self.size = size
        self.position = position

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
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Method that draws a square with '#' to the Stdout"""
        if self.__size > 0:
            for x in range(self.__position[1]):
                print()
            for x in range(self.__size):
                for y in range(self.__position[0]):
                    print(" ", end="")
                for y in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
