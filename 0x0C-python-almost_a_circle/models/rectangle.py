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
