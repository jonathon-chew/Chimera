#!/bin/bash 
gh repo list | awk '{print $1}' | sed 's/jonathon-chew\///'
