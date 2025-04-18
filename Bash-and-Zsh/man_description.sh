#!/opt/homebrew/bin/bash

if [ $1 ];
then
man "$1" | col -b | sed -n '/^NAME$/,/^[A-Z ]\{2,\}$/p' | sed ';$d' | awk -v RS= -v ORS="\n\n" 'NR<=2'
# man $1 | col -b | sed -n '/^DESCRIPTION$/,/^[A-Z ]\{2,\}$/p' | sed ';$d'
man "$1" | col -b | sed -n '/^DESCRIPTION$/,/^[A-Z ]\{2,\}$/p' | sed ';$d' | awk -v RS= -v ORS="\n\n" 'NR<=2'
else
echo "Please enter a command to look up"
fi
