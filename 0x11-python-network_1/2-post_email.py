#!/usr/bin/python3
""" This Module takes url as an argument, and fetch X-Request-Id value
"""
import urllib.request
import sys
try:
    email = sys.argv[2]
    data = {"email": email}
    data = urllib.parse.urlencode(data)
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    print(req)
    with urllib.request.urlopen(req) as response:
        value = response.read()
        print("{}".format(value.decode('utf-8')))
except Exception as e:
    print(e)
