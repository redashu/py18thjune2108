#!/usr/bin/python

import  socket
import  commands
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#   here we are  binding  current ip with  9999 port 
s.bind(("192.168.10.144",9999))

user=s.recvfrom(10)
password=s.recvfrom(10)

if  user[0] ==  'root'  and  password[0] == '123' :
	s.sendto("allow",password[1])

	while  4 >  2 :
#       receving data from client 
		data=s.recvfrom(100)
	#  showing  client ip  address
		print  data[1]
	#  processing  data in commands library 
		output=commands.getoutput(data[0])
#    sending  output to related client 
		s.sendto(output,data[1])

else :
	print   "bad user and password"
	s.sendto("login failed",password[1])
s.close()








