#!/usr/bin/python

import  commands,time

option='''
Press 1 to check Internet cable on your machine :
Press 2 to check internet access 
Press 3 to check for google acces
'''
print option

choice=raw_input()

if   choice  ==  '1'    :

	print  "plz wait internet cable is being checked by Current OS.."
        time.sleep(3)
	cable_check=commands.getoutput('sudo mii-tool  eno1')
	if  'link ok' in  cable_check:
		print  "Lan cable is COnnected"
		
	else :
		print "Cable is not COnnected"
		



elif    choice  ==  '2' :

	print  "Internet connectivity is checking in a while"

elif  choice  ==  '3'  :

	print  "loading google web page //"

else :
	print  "wrong option"









 

