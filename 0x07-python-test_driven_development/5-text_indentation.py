#!/usr/bin/python3
"""Defines a text indent function """


def text_indentation(text):
    """ Filter sentence  
    Args:
    text (str): sentence

    Raises:
        TypeError: if arguments are not string typeerror is raised   
    """
    list_of_sen = []
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    for i in text:
        if ':' in list_of_sen or '?' in list_of_sen or '.' in list_of_sen:
            print(''.join(list_of_sen).strip())
            print()
            list_of_sen = []

        if ':'not in list_of_sen or '?' not in list_of_sen or '.' not in list_of_sen:
            list_of_sen.append(i)
