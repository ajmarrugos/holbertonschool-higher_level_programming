#!/usr/bin/python3
"""
Module: 5-text_indentation.py
Doctest: 5-text_indentation.txt
"""


def text_indentation(text):
    """ Function that prints a text with 2 new lines """
    flag = True

    if type(text) != (str):
        raise TypeError("text must be a string")

    for i in text:
        if i == ' ' and flag is True:
            continue
        if i in ['.', '?', ':']:
            print(i, end="")
            print()
            print()
            flag = True
        else:
            print(i, end="")
            flag = False
