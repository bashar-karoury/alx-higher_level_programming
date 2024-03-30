#!/usr/bin/python3
""" This Module takes url as an argument, and fetch X-Request-Id value
"""
import requests
import sys
try:
    email = sys.argv[2]
    data = {"email": email}
    r = requests.post(sys.argv[1], data)
    print("{}".format(r.text))
except Exception as e:
    print(e)
