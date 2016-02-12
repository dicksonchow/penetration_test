#!/bin/bash

if [ "$#" -ne 1 ];then
	echo "Usage: $0 [/24 network address]"
	echo "Example: $0 172.15.36.0"
	echo "Example will perform a UDP ping sweep of the 172.16.36.0/24 network and output to an output.txt file"
fi

prefix=$(echo $1 | cut -d '.' -f 1-3)

for addr in $(seq 1 254);do
	hping3 $prefix.$addr --udp -c 1 2>&1 | grep 'Unreachable' | cut -d ' ' -f 5 | cut -d '=' -f 2
done
