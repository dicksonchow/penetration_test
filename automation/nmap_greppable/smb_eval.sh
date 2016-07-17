#!/bin/bash

if [ "$#" != 1 ];then
	echo "Usage: $0 [filename]"
	exit
fi

file=$1

# for x in $(grep open $file | grep 445 | cut -d" " -f 2);do
# 	nmap --script smb-check-vulns.nse -p 445 --script-args=unsafe=1 $x
# done

grep open $file | grep 445 | cut -d" " -f 2 | xargs nmap --script smb-check-vulns.nse -p 445 --script-args=unsafe=1
