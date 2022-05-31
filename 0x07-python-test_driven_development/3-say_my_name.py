#!/usr/bin/python3
"""
say_my_name:
    - Prints "My name is <first name> <last name>"
    - Checks if first_name is a string
    - Checks if last_name is a string
"""


def say_my_name(first_name, last_name=""):

    if type(first_name) != str:
        raise TypeError("first_name must be a string")

    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
