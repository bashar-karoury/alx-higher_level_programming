#!/usr/bin/env bash
# Bash script to display size of body of responce
url=$1
curl -s "$url" | wc -c
