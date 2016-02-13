#!/bin/bash

if [ "$#" -ne 3 ];then
	echo "Usage: $0 [IP-address] [First port] [Last port]"
	echo "Example: $0 172.15.36.0 1 1000"
	echo "Example will perform a TCP connection port scan on 172.16.36.0/24 from port 1 to port 1000"
	exit
fi

prefix=$(echo $1 | cut -d '.' -f 1-3)
start=$2
end=$3

for addr in $(seq 0 255);do
	echo "Scanning $prefix.$addr"
	nc -w 1 $prefix.$addr -zvn $start-$end 2>&1 | grep 'succeeded'
done
