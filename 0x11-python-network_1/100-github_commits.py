#!/usr/bin/python3
""" This Module takes url as an argument, and fetch X-Request-Id value
"""
import requests
import sys
try:
    url = " https://api.github.com/repos/{}/{}/commits?per_page=10".format(
        sys.argv[1], sys.argv[2])
    headers = {"Accept": "application/vnd.github.v3+json"}
    r = requests.get(url, headers=headers)
    if r.status_code < 400:
        results_json = r.json()
        if results_json:
            counter = 0
            commits = results_json
            for i in range(10):
                print("{}: {}".format(
                    commits[i].get("sha"),
                    commits[i].get("commit").get("author").get("name")))
        else:
            print("No result")
    else:
        print("None")
except Exception as e:
    pass
