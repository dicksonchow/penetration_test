#!/bin/bash

if [ "$#" != 2 ];then
	echo "Usage $0 [port] [filename]"
	exit
fi

port=$1
file=$2

echo "System with $port open"

grep $port $file | grep open | cut -d" " -f2
