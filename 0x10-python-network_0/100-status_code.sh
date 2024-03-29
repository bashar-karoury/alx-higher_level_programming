#!/bin/bash
# Bash script to display response of GET request
curl -s -o /dev/null -w "%{http_code}" "$1"
