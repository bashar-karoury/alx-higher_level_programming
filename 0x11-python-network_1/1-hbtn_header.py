#!/usr/bin/python3
""" This script fetch a url and displays response body
"""
import urllib.request
import sys
req = urllib.request.Request(sys.argv[1])
try:
    with urllib.request.urlopen(req) as response:
        value = response.headers["X-Request-Id"]
        print("{}".format(value))
except urllib.error.URLError as e:
    pass
