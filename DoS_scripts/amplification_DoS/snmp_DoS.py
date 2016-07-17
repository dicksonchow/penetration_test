#!/usr/bin/python

import scapy
from scapy.all import *

send(IP(dst='10.10.10.12', src='10.10.10.10')/UDP(sport=161, dport=161)/SNMP(PDU=SNMPbulk(max_repetitions=50, varbindlist=[SNMPvarbind(oid=ASN1_OID('1.3.6.1.2.1.1')), SNMPvarbind(oid=ASN1_OID('1.3.6.1.2.1.19.1.3'))])), verbose=1, count=5)
