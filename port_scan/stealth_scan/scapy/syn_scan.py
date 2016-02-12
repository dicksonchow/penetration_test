#!/usr/bin/python

import sys
import logging
logging.getLogger('scapy.runtime').setLevel(logging.ERROR)
from scapy.all import *

if len(sys.argv) != 4:
	print 'Usage: ', sys.argv[0], ' [Target-IP] [First Port] [Last Port]'
	print 'Example ', sys.argv[0], ' 10.0.0.5 1 100'
	print 'Example will TCP SYN scan ports 1 through 100 on 10.0.0.5'
	sys.exit()

ip = sys.argv[1]
start = int(sys.argv[2])
end = int(sys.argv[3])

for port in range(start, end):
	ans = sr1(IP(dst=ip)/TCP(dport=port), timeout=1, verbose=0)
	if ans == None:
		pass
	else:
		if int(ans[TCP].flags) == 18:
			print port
		else:
			pass