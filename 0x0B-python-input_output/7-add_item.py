#!/usr/bin/python3
""" Module load add save
"""


import sys
# import save_to_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
# import load_form_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# define filename
filename = "add_item.json"

# load list from file
list_a = load_from_json_file(filename)

# remove first argument, script name
args = sys.argv[1:]

# append to existed list
for a in args:
    list_a.append(a)

# save list back to file
save_to_json_file(list_a, filename)
