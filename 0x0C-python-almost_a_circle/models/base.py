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
        dict = []

        createfile = cls.__name__ + ".json"
        if list_objs is None:
            with open(createfile, 'w', encoding='utf-8') as f:
                f.write(cls.to_json_string(list_objs))

        for element in list_objs:
            dict.append(element.to_dictionary())

        with open(createfile, 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(dict))
