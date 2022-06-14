#!/usr/bin/python3
"""
Mudule: base.py
Unittest: tests/test_base.py
"""


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of a Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
