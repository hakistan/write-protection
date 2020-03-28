#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess,sys


into_msg = '''
###################################################################
#       Hakistan's USB Read-Write Protection Script               #
#                                                                 #
# This Script is Developed by Hakistan.                           #
#                                                                 #
# Support and Join Our Community to learn Cyber Security          #
# and to get more amazing tools like this one.                    #
#                                                                 #
# Find Us on Telegram: https://t.me/hakistan                      #
# OR                                                              #
# Find Us on Youtube: https://www.youtube.com/hakistan            #
#                                                                 #
# Our Repo on Github: https://www.github.com/hak15stan            #
#                                                                 #
# If you have Suggetions or new ideas for us, than let us know.   #
#                                                                 #
###################################################################
'''

print(into_msg)


def EWMode():
	commands=b'''
	list volume
	'''
	process = subprocess.Popen('C:\\WINDOWS\\system32\\diskpart.exe', stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
	out,err = process.communicate(commands)

	output = out.decode("utf-8")

	print(output.replace("DISKPART>"," "))

	number = input("Enter volume No.> ")

	#print(number)

	process = subprocess.Popen('C:\\WINDOWS\\system32\\diskpart.exe', stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
	commands = '''
	select volume {vs}
	attributes disk set readonly
	exit
	'''.format(vs=number)
	#print(commands)
	my_str_as_bytes = str.encode(commands)
	out,err = process.communicate(my_str_as_bytes)
	outputstring = out.decode("utf-8").replace("DISKPART>"," ").replace("Leaving DiskPart..."," ").strip()
	#stingend = outputstring.replace("Microsoft DiskPart version 10.0.18362.1","").replace("Copyright (C) Microsoft Corporation.","").replace("Copyright (C) Microsoft Corporation.","").strip()
	postString = outputstring.split("\n",6)[6];
	print("\n"+postString)

def DWMode():
	commands=b'''
	list volume
	'''
	process = subprocess.Popen('C:\\WINDOWS\\system32\\diskpart.exe', stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
	out,err = process.communicate(commands)

	output = out.decode("utf-8")

	print(output.replace("DISKPART>"," "))

	number = input("Enter volume No.> ")

	#print(number)

	process = subprocess.Popen('C:\\WINDOWS\\system32\\diskpart.exe', stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
	commands = '''
	select volume {vs}
	attributes disk clear readonly
	exit
	'''.format(vs=number)
	#print(commands)
	my_str_as_bytes = str.encode(commands)
	out,err = process.communicate(my_str_as_bytes)
	outputstring = out.decode("utf-8").replace("DISKPART>"," ").replace("Leaving DiskPart..."," ").strip()
	#stingend = outputstring.replace("Microsoft DiskPart version 10.0.18362.1","").replace("Copyright (C) Microsoft Corporation.","").replace("Copyright (C) Microsoft Corporation.","").strip()
	postString = outputstring.split("\n",6)[6];
	print("\n"+postString)

optmode = input("Enter 1 to enable write protect or 2 to disable > ")

if optmode == "1":
	EWMode()

elif optmode == "2":
	DWMode()

else:
	sys.exit("Invalid Option. Exting...")

