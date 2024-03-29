#!/usr/bin/python3
""" This Module takes url as an argument, and fetch X-Request-Id value
"""
import requests


import sys
try:
    r = requests.get(sys.argv[1])
    value = r.headers['X-Request-Id']
    print("{}".format(value))
except Exception as e:
    pass
