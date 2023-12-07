#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    temp_dictionary = a_dictionary.copy()
    for k, v in temp_dictionary.items():
        if v == value:
            del a_dictionary[k]
    return a_dictionary
