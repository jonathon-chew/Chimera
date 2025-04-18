#!/bin/bash
find $HOME/Documents/Scripts -type d -name ".git" | while read gitdir; do
    repo_dir="$(dirname "$gitdir")"
    cd "$repo_dir" || continue
    remote_url=$(git remote get-url origin 2>/dev/null)
    if [ -n "$remote_url" ]; then
        echo "$repo_dir
$remote_url
" >> $HOME/Documents/Scripts/Git/remote_url_locations.txt
    fi
done
