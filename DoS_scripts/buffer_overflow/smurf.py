#!/usr/bin/python

import scapy

send(IP(dst='10.10.10.255', src='10.10.10.10')/ICMP(), count=100, verbose=1)
