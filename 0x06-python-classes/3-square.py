#!/usr/bin/python3
"""Square class with definition
includes a size instance/attribute
includes TypeError & ValueError exceptions
includes a area method functon
"""


class Square:
    """Represents an empty square"""
    def __init__(self, size=0):
        """
        Init class with args: size
        runs a check to ensure size data is correct type and value.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Method function to return the area of the Square"""
        return (self.__size * self.__size)
