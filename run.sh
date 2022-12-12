#!/bin/zsh

if [ $# -lt 2 ]
  then
    echo "Not enough arguments."
    echo "   Expected a year number [4 digits] and a task number [2 digits] at least."
    exit 0
fi

if [ $# -eq 2 ]
  then
    python3 $1/$1.$2.py
  else
    python3 $1/$1.$2.py $3
fi