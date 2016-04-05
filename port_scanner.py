#!/usr/bin/env python
import socket
import sys
import subprocess
from datetime import datetime

# clear the screen
subprocess.call('clear',shell=True)

# Ask for input
remoteServer = raw_input("Enter the hostname:")
remoteServerIP = socket.gethostbyname(remoteServer)

#print a nice banner 

print("-"*60)
print("Please wait scanning remote host",remoteServerIP)
print("-"*60)

# check what time the scan started

t1 = datetime.now()

# Using the range function to specify ports (1 to 1024)

# We try to catch some errors

try:
	for port in range(1,1025):
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		result = sock.connect_ex((remoteServerIP,port))
		if result == 0:
			print("Port{}:\t Open".format(port))
			sock.close()
		else:
			print("Port{}:\t Close".format(port))
			sock.close()

except KeyboardInterrupt:
	print("You pressed Ctrl+C")
	sys.exit()
except socket.gaierror:
	print("Hostname could not be resolved. Existing")
	sys.exit()
except socket.error:
	print("Couldn't connect to server")
	sys.exit()

# Checking the time again

t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script

total = t2-t1

# Printing the information to screen

print("Scanning Complet4ed in:",total)







 

