#!/bin/bash

# Script which displays color is the 256-color palette along with 
# ANSI code in XTerm/ANSI-compatible terminals with 256-color 
# palette support

# Script taken from https://askubuntu.com/questions/558280/changing-colour-of-text-and-background-of-terminal

for((i=16; i<256; i++)); do
    printf "\e[48;5;${i}m%03d" $i;
    printf '\e[0m';
    [ ! $((($i - 15) % 6)) -eq 0 ] && printf ' ' || printf '\n'
done
