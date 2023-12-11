#!/bin/zsh

new_results=$(find $PWD/* -type f -iname "*$1*"); new_array=("${(@f)new_results}"); for i in "${new_array[@]}"; do; open "$i"; done
