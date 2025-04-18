#!/bin/zsh

#Turns the title into the name of the folder a user is in IF a title is not provided, otherwise it uses what ever is offered.

func newTitle() {
  if [ $1 ];
  then
    echo $1
    echo -en "\033]1; $1 \007" 
  else
  local pwd="${PWD/#$HOME/~}"
  pwd_list=(${(s:/:)pwd})
  pwd_list=('/' $pwd_list)
  echo $pwd_list[${#pwd_list}]
    echo -en "\033]1; $pwd_list[${#pwd_list}] \007" 
  fi
}
