#!/usr/bin/python3
"""
Module: 12-pascal_triangle.py
"""


def pascal_triangle(n):
    """ Will print a pascal triangle with the size of 'n' """

    matrix = []
    prev = []

    for i in range(n):
        to_list = []
        x = -1
        y = 0
        for j in range(len(prev) + 1):
            if x == -1 or y == len(prev):
                to_list += [1]
            else:
                to_list += [prev[x] + prev[y]]
            x += 1
            y += 1
        matrix.append(to_list)
        prev = to_list[:]

    return matrix
