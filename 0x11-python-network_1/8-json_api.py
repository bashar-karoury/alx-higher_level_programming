#!/usr/bin/python3
""" This Module takes url as an argument, and fetch X-Request-Id value
"""
import requests
import sys
try:
    data = {}
    if len(sys.argv) >= 2:
        data = {"q": sys.argv[1]}
    else:
        data = {"q": ""}
    r = requests.post("http://0.0.0.0:5000/search_user", data)

    if r.status_code < 400:
        results_json = r.json()
        if results_json:
            print("[{}] {}".format(results_json['id'], results_json['name']))
        else:
            print("No result")
# except requests.exceptions.JSONDecodeError as e:
#    print("Not a valid JSON")

except Exception as e:
    print("Not a valid JSON")
