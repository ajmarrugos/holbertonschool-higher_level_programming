#!/usr/bin/python3
"""
Module: 8-class_to_json.py
"""


def class_to_json(obj):
    """ Returns the dictionary description for JSON """

    return obj.__dict__
