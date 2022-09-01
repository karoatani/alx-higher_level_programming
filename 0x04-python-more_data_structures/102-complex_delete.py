#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    store_key = ''
    for k, v in a_dictionary.items():
        if value == v:
            store_key = k
        del a_dictionary[store_key]
        return a_dictionary
    return a_dictionary
