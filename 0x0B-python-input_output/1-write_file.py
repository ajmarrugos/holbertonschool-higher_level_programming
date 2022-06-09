#!/usr/bin/python3
"""
Module: 1-write_file.py
"""


def write_file(filename="", text=""):
    """ Function will write to file """
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)
