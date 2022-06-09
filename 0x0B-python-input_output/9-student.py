#!/usr/bin/python3
"""
Module: 9-student.py
"""


class Student:
    """ Representation of a student """
    def __init__(self, first_name, last_name, age):
        """ Constructor for Student Object """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Will return a dictionary representation of a
        Student instance with specified attributes """
        return self.__dict__
