#!/bin/bash
# Bash script to display response of GET request
curl -sX POST -F "file=$2" "$1"
