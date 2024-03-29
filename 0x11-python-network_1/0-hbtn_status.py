#!/usr/bin/python3
""" This script fetch a url and displays response body
"""
import urllib.request

req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
try:
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(the_page)))
        print("\t- content: {}".format(the_page))
        print("\t- utf8 content: {}".format(the_page.decode('utf-8')))
except urllib.error.URLError as e:
    pass
