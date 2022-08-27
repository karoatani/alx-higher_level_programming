#!/usr/bin/python3
from copy import copy


def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return my_list.copy()
    cp_list = my_list[:]
    for i in cp_list:
        cp_list[idx] = element
    return cp_list
