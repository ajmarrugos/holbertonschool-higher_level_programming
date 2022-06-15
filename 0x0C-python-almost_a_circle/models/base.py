#!/usr/bin/python3
"""
Mudule: base.py
Unittest: tests/test_base.py
"""

import json


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a Base instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Will return a JSON string of a dictionary"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Will save JSON strinf of a list of objects to a file"""
        if list_objs is None or list_objs == []:
            tofile = "[]"
        else:
            tofile = cls.to_json_string([o.to_dictionary() for o in list_objs])
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(tofile)

    @staticmethod
    def from_json_string(json_string):
        """Will convert JSON string into a dictionary"""
        dict = []
        if json_string is None or json_string == "":
            return dict
        dict = json.loads(json_string)
        return dict

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance from a temp scratch"""
        if cls.__name__ == "Rectangle":
            temp = cls(1, 1)
        if cls.__name__ == "Square":
            temp = cls(1)

        temp.update(**dictionary)
        return temp
