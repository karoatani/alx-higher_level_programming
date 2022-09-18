#!/usr/bin/python3
"""Defines a function to divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """ Divides matrix
    Args:
    matrix (array): array of numbers
    div (int): integer or float

    Raises:
        TypeError: if arguments are not either int or float typeerror is raised 
                    or length of row not thesame 
    """
    new_set = set()
    for i in matrix:
        for ele in i:
            if not isinstance(ele, int) or isinstance(ele, float):
                raise TypeError(
                    'matrix must be a matrix (list of lists) of integers/floats')
        new_set.add(len(i))

    if len(new_set) != 1:
        raise TypeError('Each row of the matrix must have the same size')

    if not isinstance(ele, int) or isinstance(ele, float):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_list = [[round(ele/div, 2) for ele in i]for i in matrix]

    return new_list
