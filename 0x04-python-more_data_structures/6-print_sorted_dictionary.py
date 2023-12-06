#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    sorted_keys = list(a_dictionary)
    sorted_keys.sort()
    for k in sorted_keys:
        print("{0}: {1}".format(k, a_dictionary[k]))    
