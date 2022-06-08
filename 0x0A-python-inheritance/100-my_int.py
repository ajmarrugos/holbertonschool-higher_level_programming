#!/usr/bin/python3
""""
Module: 100-my_int.py
"""


class MyInt(int):
    """ Class inheriting from int, with reverse behavior """

    def __eq__(self, other):
        """ Equality becomes inequality """

        return super().__ne__(other)

    def __ne__(self, other):
        """ Inequality becomes equality """

        return super().__eq__(other)
