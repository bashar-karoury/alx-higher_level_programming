#!/usr/bin/python3
""" This Module takes url as an argument, and fetch X-Request-Id value
"""
import requests
import sys
try:
    url = "https://api.github.com/users/{}".format(sys.argv[1])
    auth_token = "token {}".format(sys.argv[2])

    headers = {'Authorization': auth_token}
    r = requests.get(url, headers=headers)

    if r.status_code < 400:
        results_json = r.json()
        if results_json:
            print("{}".format(results_json['id']))
        else:
            print("No result")
    else:
        print("None")
except Exception as e:
    print("Not a valid JSON")
