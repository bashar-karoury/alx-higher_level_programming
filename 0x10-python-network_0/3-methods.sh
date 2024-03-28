#!/bin/bash
# Bash script to display response of GET request
curl -sX OPTIONS -I "$1" | grep "Allow" | cut -d: -f2 2> /dev/null 
