#!/usr/bin/python3
"""
Module: 2-matrix_divided.py
Doctest: 2-matrix_divided.txt
"""


def matrix_divided(matrix, div):
    """ Recives a 2D matrix and a division number """

    """ Declares error messages as string variables to short syntax """
    div_zero = "division by zero"
    div_numb = "div must be a number"
    wrg_size = "Each row of the matrix must have the same size"
    not_mtrx = "matrix must be a matrix (list of lists) of integers/floats"

    """ Declares a new matrix as an array """
    new_mtrx = []

    """ Checks if "div" is 0 """
    if div == 0:
        raise ZeroDivisionError(div_zero)

    """ Checks if "div" is an int or float """
    if not isinstance(div, (int, float)):
        raise TypeError(div_numb)

    """ Checks if each list in the matrix are the same size """
    for lists in matrix:
        if len(lists) != len(matrix[0]):
            raise TypeError(wrg_size)
            inner_list = []
    """ Checks if the entire matrix is made of ints/floats """
    for items in lists:
        if not isinstance(items, (int, float)):
            raise TypeError(not_matrix)
        else:
            """ Divides the items of the matrix of numbers by a number """
            inner_list.append(round(items / div, 2))

    new_mtrx.append(inner_list)

    return new_mtrx
