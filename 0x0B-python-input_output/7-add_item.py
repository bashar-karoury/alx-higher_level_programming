#!/usr/bin/python3
""" Module that continas scirpt to add args to a python list
    and then save them to a file
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

list_a = []
for a in sys.argv:
    list_a.append(a)
del list_a[0]
filename = "add_item.json"
save_to_json_file(list_a, filename)
