#!/usr/bin/python3
"""
Module: 2-append_write.py
"""


def append_write(filename="", text=""):
    """ Function will append to a file """
    with open(filename, 'a', encoding='utf=8') as f:
        return f.write(text)
