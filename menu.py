#!/usr/bin/python2
import  time
import  webbrowser
menu='''
Press  1  to check  current  time and date  :
Press  2  to scan all your Mac address in you current connected Network  :
PRess  3   to shutdown your machine after 15 minutes :
Press  4  To search something on Google :
Press  5  to Logout your current machine :
Press  6  to Shutdown all connected system in your current network :
Press  7  to update  status in facebook  :
Press  8   to  list  ip address of  given website : 
'''
print  menu
choice=raw_input()

if  choice  ==  '1' :
	print  "current date and time is :   ",time.ctime()

elif  choice  ==  '4' :
	find=raw_input("enter your query : ")
	webbrowser.open_new_tab("https://www.google.com/search?q="+find)
else :
	print  "Invalid OPtion"

 
