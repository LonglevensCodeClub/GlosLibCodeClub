#!/usr/bin/env python3
#########################################################
#
# Logic Programming - Simple IF
#
#########################################################
from logicUtils import *

##########
#
# Here we have defined a function for checking hunger
# this function is then called below
#
##########
def checkfat():
	fat = askQuestion(" are you fat")

	print("fat: " + str(fat))

	if (fat):
		# go on a diet? Print a message to tell you the answer.
		print("go on a diet!")
	else:
		# go on a diet? Print a message to tell you the answer.
		print("yes you are")

## You can comment this out when you just want to run your own questions below
checkfat()

##########
#
# Exercise: Write another question that asks
#	* 'are feeling cold?'
# If you are feeling cold, the program will suggest
#	* 'please put a jumper on'
# otherwise it can just say
#	* 'i'm glad you are comfortable'
#
##########
