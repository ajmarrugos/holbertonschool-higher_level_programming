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

    def update(self, *args, **kwargs):
        """Updates square values"""
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                setattr(self, k, v)
        elif len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            print()

    def __str__(self):
        """Returns a string representation of a Square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        """Returns a dictionary from attribute data"""
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
