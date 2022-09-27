#!/usr/bin/python3
"""Define a function to list of available attributes and methods of an object"""


def lookup(obj):
    """List all available attributes and methds of a object"""
    return [i for i in obj.__dict__]
