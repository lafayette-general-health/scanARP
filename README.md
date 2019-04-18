# scanARP
Checks to determine if a MAC address shows up on the wrong VLAN.  This is useless to 99% of people, but incase you wanted to see how we do it, here it is.

Why do I use this script?  

In this scenario I've got a bunch of wireless devices all of the same type across several facilities.  Those wireless devices all connect to same SSID, however, each facility's APs are contained in their own AP Group where the SSID is assigned a different interface in my controller.  Facility 1 is on VLAN 13 and Facility 2 is on VLAN 16.  The vendor is running reports on the devices and classifying their devices into locations based on IP.
*************************
(Quick aside to the devs who created this reporting system I will say this to you):

BOOOOOOOO!!!! THIS IS A STUPID WAY OF IDENTIFYING THE LOCATION OF A DEVICE IN A CONTROLLER BASED WIRELESS ENVIRONMENT!  THERE ARE TOO MANY FACTORS TO CONSIDER WHEN USING A LOGICAL ADDRESS TO IDENTIFY A PHYSICAL LOCATION!!!! 
INSTEAD, SIMPLY USE PHYSICAL INFORMATION OF THE UNIT [MAC OR SERIAL NUMBER]!!!!  
ESPECIALLY SINCE YOU REQUIRE DHCP, THEN KEY IN ON INFORMATION THAT CONSTANTLY CHANGES!!!  
STUPID! YOU'LL END UP EXACTLY WHERE WE ARE NOW AND WHY I HAD TO WRITE THIS SCRIPT

![alt-text](https://memegenerator.net/img/instances/58461592/you-big-dummy.jpg)

/end rant
*************************

So what we have found is that MACs that match the pattern 00:17:23:31 or 00:17:23:32 match the MAC addresses of all the devices at facility 2.  The devices at facility 1 are all 00:17:23:33 or 00:17:23:34.  Therefore in this script I am checking the ARP table of the SSID assigned at facility 1 for any MAC that would normally appear at facility 2.  I am doing this because reporting data is showing devices at facility 2 on reports for facility 1, which is causing the vendor to BLAME THE NETWORK for assigning bad IP addresses to the devices at Facility 2 (in other words they are claiming I am putting devices at facility 2 on facility 1's VLAN, causing the inaccurate reports to occur).  This is nonsense, but being the litigious network engineer that I am, I have decided to poll my gateways every 60 seconds to assure that this is not happening.
