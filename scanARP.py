#!/usr/bin/python
import subprocess
import time
import os
import sys

#DEFINE CONSTANTS
#-------------------------------#
#READ COMMUNITY STRING
READSNMP = "public"
#-------------------------------#
#EXAMPLE MAC FORMAT HERE, OUI+trailing chars of MAC.  badMAC signifies that you are looking
#for that pattern inside of a VLAN where it is not supposed to belong.  
#i.e.- Pattern "00:17:23:3[1-2]" should NOT be found in arp table of interface X:
OUI = '0:17:23:'
BADMAC = '3[1-2]'
#-------------------------------#
#IP address of gateway where ARP table resides
TARGET = "1.1.1.1"
#SNMP Index# of interface where MAC should NOT be found
INDEX = "151060493"

#Bash command that asks target device via SNMP v2c for ARP Table of VLAN specified as follows:
#-------------------------------#
#Return count of number of offending MACs in the ARP Table
CMD = "snmpwalk -v2c -c {0} {1} IP-MIB::ipNetToMediaPhysAddress.{2} | grep '{3}{4}' | wc -l".format(READSNMP,TARGET,INDEX,OUI,BADMAC)
#Return ARP Table results from SNMP poll matching offending MACs
CMD2 = 'snmpwalk -v2c -c {0} {1} IP-MIB::ipNetToMediaPhysAddress.{2} | grep "{3}{4}"'.format(READSNMP,TARGET,INDEX,OUI,BADMAC)
#Return ARP Table results from SNMP poll matching OUI 
CMD3 = 'snmpwalk -v2c -c {0} {1} IP-MIB::ipNetToMediaPhysAddress.{2} | grep "{3}"'.format(READSNMP,TARGET,INDEX,OUI)
#-------------------------------#

#write PID of process so you can easily kill it if it runs in background <command would be "kill $(cat scanARP.pid)">
def writePidFile():
    pid = str(os.getpid())
    f = open('scanARP.pid', 'w')
    f.write(pid)
    f.close()

#An infinite loop that SNMP polls gateway for ARP information
def scanARP():
	while True:
      #poll number of items in ARP table that are offending MACs
			count = subprocess.Popen(CMD, shell=True, stdout=subprocess.PIPE)
      #poll ARP table of specific interface for devices matching particular OUI and print results
			table =  subprocess.Popen(CMD3, shell=True, stdout=subprocess.PIPE)
			tout = (table.communicate()[0])
			print '\n'+tout
	    #If number of offending MACs is greater than 0, write arp table to file and exit routine.
			if out <> 0:
					ARPTable = ''
					f = open("MACs.txt","a")
					ARPTable = subprocess.Popen(CMD2, shell=True, stdout=subprocess.PIPE)
					arp = ARPTable.communicate()[0]
					print "ANOMOLY OCCURED: \n"+arp
					f.write(arp)
					break
      #Now you wait just a minute
			time.sleep(60)
			print "\n******\nARP SCAN!\n******\n"
			sys.stdout.flush()

writePidFile()
scanARP()
