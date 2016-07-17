#!/usr/bin/python

import logging
logging.getLogger('scapy.runtime').setLevel(logging.ERROR)
from scapy.all import *

def rules(pkt):
	try:
		if (pkt[IP].dst == '10.10.10.11') and (pkt[ICMP]):
			print str(pkt[IP.src]) + 'is exploitable'
	except:
		pass

print 'Listening for incoming ICMP traffic. Use CTRL+C to stop listening'

sniff(lfilter=rules, store=0)
