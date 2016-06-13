#!/usr/bin/python

import sys
import logging
from scapy.all import *
logging.getLogger('scapy,runtime').setLevel(logging.ERROR)

if len(sys.argv) != 3:
	print 'Usage - {} [Target-IP] [Target-Port]'.format(sys.argv[0])
	print 'Example = {} 10.0.0.5 443'.format(sys.argv[0])
	print 'Example will determine if filtering exists on port 443 of host 10.0.0.5'
	sys.exit()

ip = sys.argv[1]
port = int(sys.argv[2])

ACK_response = sr1(IP(dst=ip)/TCP(dport=port, flags='A'), timeout=1, verbose=0)
SYN_response = sr1(IP(dst=ip)/TCP(dport=port, flags='S'), timeout=1, verbose=0)

if (ACK_response == None) and (SYN_response == None):
	print 'Port is either unstatefully filtered or host is down.'
elif ((ACK_response == None) or (SYN_response == None)) and not ((ACK_response == None) and (SYN_response == None)):
	print 'Stateful filtering in place'
elif int(SYN_response[TCP].flags) == 18:
	print 'Port is unfiltered and open'
elif int(SYN_response[TCP].flags) == 20:
	print 'Port is unfiltered and closed'
else:
	print 'Unable to determine if the port is filtered'
