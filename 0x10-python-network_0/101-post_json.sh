#!/bin/bash
# Bash script to display response of GET request
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
