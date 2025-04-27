#!/bin/bash

found=false

for i in */ ; do
    # Check if it's a directory and has a .git folder
    if [ -d "$i/.git" ]; then
        cd "$i" || continue
        echo "$i Last Updated: $(git log -1 --format="%cd")"
        found=true
        cd ..
    fi
done

if [ "$found" = false ]; then
  echo "No git folders where found"
fi
