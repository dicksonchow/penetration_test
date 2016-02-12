#!/bin/bash

if [ "$#" -ne 1 ];then
	echo "Usage - $0 [/24 network address]"
	echo "Example - $0 172.16.36.0"
	echo "Example will perform an ICMP ping sweep of the 172.16.36.0/24 network and output to an output.txt file"
	exit
fi

prefix=$(echo $1 | cut -d "." -f 1-3)

for addr in $(seq 1 254);do
	hping3 $prefix.$addr --icmp -c 1 2>&1 | grep 'len' | cut -d " " -f 2
done
