#!/usr/bin/python

import  socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


u=raw_input("enter username : ")
p=raw_input("password check : ")

s.sendto(u,("192.168.10.144",9999))
s.sendto(p,("192.168.10.144",9999))
#  checking  responce from server  
response=s.recvfrom(20)
if  response[0]   ==  "allow" :

	while  4 >  2 :
		msg=raw_input("enter any command   : ")
		s.sendto(msg,("192.168.10.144",9999))
		print  s.recvfrom(10000)

else :
	print  response[0]


s.close()


