#!/usr/bin/python

import logging
logging.getLogger('scapy.runtime').setLevel(logging.ERROR)
from scapy.all import *


def get_ipid(destination):
	try:
		reply = sr1(IP(dst=destination)/TCP(flags='SA'), timeout=2, verbose=0)
		return int(reply[IP].id)
	except:
		print 'Something went wrong!'


def test_zombie(zombie):
	init_val = get_ipid(zombie)
	end_val = get_ipid(zombie)
	if (end_val - init_val) == 1:
		print 'IPID sequence is increased by 1.'
		print zombie, 'seems to be a good zombie.'
		choice = raw_input('Use this system as a zombie? (Y or N): ')
		if choice == 'Y':
			zombiescan(prompt_for_target(), zombie)
	else:
		print 'IPID sequence is not increated by 1.'
		print 'start value: ', init_val
		print 'end value', end_val
		print 'Please try another host to see if it is a good zombie.'


def zombiescan(target, zombie):
	print '\nScanning target: ', target, ' \nwith zombie: ', zombie
	print '\n---------- Open Ports of Target ----------\n'
	
	for port in range(1, 1000):
	
		init_val = get_ipid(zombie)
		send(IP(src=zombie, dst=target)/TCP(flags='S', dport=port), verbose=0)
		end_val = get_ipid(zombie)
		
		if (end_val - init_val) == 2:
			print port


def prompt_for_target():
	return raw_input('Enter the IP address of the target system: ')


print '---------- Zombie Scan Suite ----------\n'
print '1. - Identify Zombie Host\n'
print '2. - Perform Zombie Scan\n'
ans = raw_input('Select an option (1 or 2): ')

if ans == '1':
	zombie = raw_input('Enter the IP address of a system for testing: ')
	test_zombie(zombie)
elif ans == '2':
	zombie = raw_input('Enter the IP address of the zombie system: ')
	target = prompt_for_target()
	zombiescan(target, zombie)
else:
	print 'Use your ass to read the instructions.'