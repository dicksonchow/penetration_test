#!/usr/bin/python

import scapy
from scapy.all import *

send(IP(dst='208.67.220.220', src='192.168.1.21')/UDP()/DNS(rd=1, qdcount=1, qd=DNSQR(qname='google.com', qtype=255)), verbose=1, count=2)
