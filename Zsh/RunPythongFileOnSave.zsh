#!/bin/zsh

#file=/Users/hunteradder626/Library/CloudStorage/OneDrive-Personal/Home/Finance/Finance.py

file=$1
if [ $1 ];
then;
  echo "Running file: " $file
  oldTime=$(date -r $file +%s);
  while True
  do;
    lastModificationSeconds=$(date -r $file +%s);
    if [[ $oldTime -lt $lastModificationSeconds ]];
    then;
      oldTime=$lastModificationSeconds;
      echo $(date)
      python3 $file ;
      sleep 2
    fi;
  done;
#else;
#  echo "No file was provided"
fi;
