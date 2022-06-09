#!/usr/bin/python3
"""
Module: 4-from_json_string.py
"""


import json


def read_file(filename=""):
    """ Opens and prints file contents to stdout """

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
