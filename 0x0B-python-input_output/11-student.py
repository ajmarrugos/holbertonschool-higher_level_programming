#!/usr/bin/python3
"""
Module: 11-student.py
"""


class Student:
    """ Representation of a student """
    def __init__(self, first_name, last_name, age):
        """Constructor for Student Object """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Will return a dictionary representation of a
        Student instance with specified attributes """
        if attrs is None:
            return(self.__dict__)

        return({item: self.__dict__[item] for item
                in attrs if item in self.__dict__})

    def reload_from_json(self, json):
        """ Replaces all attributes of the Student instance """
        for atr in json:
            self.__dict__[atr] = json[atr]
