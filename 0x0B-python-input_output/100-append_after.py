#!/usr/bin/python3
"""
Module: 100-append_after.py
"""


def append_after(filename="", search_string="", new_string=""):
    """ Apends a new line to a file when a string is found """

    with open(filename, 'r') as f:
        file = f.readlines()

    new_file = ""
    for line in file:
        new_file += line
        if search_string in line:
            new_file += new_string

    with open(filename, 'w') as f:
        f.write(new_file)
