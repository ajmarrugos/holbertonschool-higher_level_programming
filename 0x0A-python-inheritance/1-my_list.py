#!/usr/bin/python3
"""
Module: 1-my_list.py
Doctest: 1-my_list.txt
"""


class MyList(list):
    """ Class MyList inherits from list """

    def print_sorted(self):
        """ Will print the list stored in accending order """

        print(sorted(self))
