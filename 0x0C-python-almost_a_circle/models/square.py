#!/usr/bin/python3
"""
Mudule: square.py
Unittest: tests/test_square.py
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Initializes a Square instance"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Returns the size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size attribute"""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns a string representation of a Square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
