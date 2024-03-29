#!/usr/bin/python3
""" This Module takes url as an argument, and fetch X-Request-Id value
"""
import urllib.request
import sys
try:
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        print("{}".format(response.read().decode('utf-8')))
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))
except Exception as e:
    pass
