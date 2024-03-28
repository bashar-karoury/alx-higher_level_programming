#!/bin/bash
# Bash script to display response of GET request
curl -sX OPTIONS -I "$1" | grep "^Allow:\s" | sed 's/^Allow:\s//'
