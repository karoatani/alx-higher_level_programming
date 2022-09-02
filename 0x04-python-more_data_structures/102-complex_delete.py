#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value in a_dictionary.values():
        store_key = []
        for k, v in a_dictionary.items():
            if v == value:
                store_key.append(k)
        for i in store_key:
            del a_dictionary[i]
        return a_dictionary
    return a_dictionary
# return dict(filter(lambda v: value not in v, a_dictionary.items()))
