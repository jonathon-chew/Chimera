#!/bin/zsh

((x=1)); for i in *; do; echo $x $i; ((x=x+1)); done
