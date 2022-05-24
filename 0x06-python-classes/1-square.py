#!/usr/bin/python3
"""Square class definition with an instance"""


class Square:
    """Represents an empty square"""
    def __init__(self, size):
        """Initializes a square
        Args:
            size (int): size of a side of the square
        Returns: None
        """
        self.__size = size
