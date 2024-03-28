#!/bin/bash
# Bash script to display response of GET request
curl -f -L -X GET "$1" 2> /dev/null
