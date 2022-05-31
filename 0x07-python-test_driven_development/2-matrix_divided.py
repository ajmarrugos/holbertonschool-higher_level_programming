#!/usr/bin/python3
"""
matrix_divided:
    - Divides each element of a matrix of numbers by a number
    - Checks if the entire list is int/float
""" 
"""Defined errors"""
    err_type = "matrix must be a matrix (list of lists) of integers/floats"
    err_size = "Each row of the matrix must have the same size"


def matrix_divided(matrix, div):

    if not isinstance(matrix, list):
        raise TypeError(err_type)
    if len(matrix) == 0:
        raise TypeError(err_type)

    new_matrix = []
    
    if isinstance(matrix[0], bool):
        raise TypeError(err_type)
    try:
        len_fst_row = len(matrix[0])
    except Exception:
        raise TypeError(err_type)

    for list_x in matrix:
    
        new_matrix.append(list(map(lambda n: round(n/div, 2), list_x)))

    return new_matrix
