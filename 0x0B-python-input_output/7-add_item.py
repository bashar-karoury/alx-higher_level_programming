#!/usr/bin/python3
""" Module load add save """
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
list_a = load_from_json_file(filename)
args = sys.argv[1:]
for a in args:
    list_a.append(a)
save_to_json_file(list_a, filename)
