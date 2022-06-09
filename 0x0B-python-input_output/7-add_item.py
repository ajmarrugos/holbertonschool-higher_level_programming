#!/usr/bin/python3
"""
Module: 7-add_item.py
"""

from os import path
from sys import argv as av
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item(filename="add_item.json"):
    """
    Will Add all arguments to a Python list,
    and then save them to a file.
    """

    if __name__ == "__main__":
        to_file = "add_item.json"
        buff = []

        if path.isfile(to_file):
            buff = load_from_json_file(to_file)

        buff.extend(av[1:])
        save_to_json_file(buff, to_file)
