#!/usr/bin/python

import logging
logging.getLogger('scapy.runtime').setLevel(logging.ERROR)
from scapy.all import *

SYN = IP(dst='10.10.10.10')/TCP(dport=4444, flags='S')

print '--- SENT ---'
SYN.display()

print '\n\n--- RECEIVED ---'
res_1 = sr1(SYN, timeout=1, verbose=0)
res_1.display()

if int(res_1[TCP].flags) == 18:
	print '\n\n--- SENT ---'
	ACK = IP(dst='10.10.10.10')/TCP(dport=4444, flags='A', ack=(res_1[TCP].seq + 1))
	res_2 = sr1(ACK, timeout=1, verbose=0)
	ACK.display()
	print '\n\n--- RECEIVED ---'
	res_2.display()
else:
	print 'SYN-ACK not returned'