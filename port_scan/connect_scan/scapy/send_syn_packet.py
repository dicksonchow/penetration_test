#!/usr/bin/python

import logging
logging.getLogger('scapy.runtime').setLevel(logging.ERROR)
from scapy.all import *

response = sr1(IP(dst='10.10.10.11')/TCP(dport=80, flags='S'))
reply = sr1(IP(dst='10.10.10.11')/TCP(dport=80, flags='A', ack=(response[TCP].seq + 1)))
