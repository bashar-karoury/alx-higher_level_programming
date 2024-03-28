#!/bin/bash
# Bash script to display size of body of responce
curl -s "$1" | wc -c
