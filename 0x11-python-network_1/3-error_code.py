#!/usr/bin/python3
""" This Module takes url as an argument, and fetch X-Request-Id value
"""
import urllib.request
import sys
try:
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        print("{}".format(response.read()))
except urllib.error.HTTPError as e:
    print(e.code)
except Exception as e:
    pass
