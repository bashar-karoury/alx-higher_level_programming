#!/usr/bin/python3
""" This Module takes url as an argument, and fetch X-Request-Id value
"""
import requests

r = requests.get('https://alx-intranet.hbtn.io/status')
print("Body response:")
print("\t- type: {}".format(type(r.text)))
print("\t- content: {}".format(r.text))
