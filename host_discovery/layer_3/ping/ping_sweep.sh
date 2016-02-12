#!/bin/bash

if [ "$#" -ne 1 ];then
	echo "Usage: $0 [/24 network address]"
	echo "Example: $0 172.16.36.0"
	echo "Example will perform an ICMP ping sweep of the 172.16.36.0/24 network"
	exit
fi

prefix=$(echo $1 | cut -d '.' -f 1-3)

for addr in $(seq 0 254);do
	ping -c 1 $prefix.$addr | grep "bytes from" | cut -d " " -f 4 | tr -d ':' &
done
