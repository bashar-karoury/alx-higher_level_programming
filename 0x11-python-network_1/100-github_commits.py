#!/usr/bin/python3
""" This Module takes url as an argument, and fetch X-Request-Id value
"""
import requests
import sys
try:
    url = " https://api.github.com/repos/{}/{}/commits?per_page=10".format(
        sys.argv[1], sys.argv[2])
    headers = {"Accept": "application/vnd.github.v3+json"}
    print(url)
    r = requests.get(url, headers=headers)
    if r.status_code < 400:
        results_json = r.json()
        if results_json:
            counter = 0
            for commit in results_json:
                if counter >= 10:
                    break
                author = commit['commit']['author']
                print("{}: {}".format(commit['sha'], author['name']))
                counter += 1
        else:
            print("No result")
    else:
        print("None")
except Exception as e:
    pass
