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
def checkHunger():
	hungry = askQuestion("Are you feeling cold?")

	print("cold: " + str(hungry))

	if (hungry):
		# Should you eat something? Print a message to tell you the answer.
		print("You should put on a jumper!")
	else:
		# Should you eat something? Print a message to tell you the answer.
		print("i'm glad you are comfortable!")

## You can comment this out when you just want to run your own questions below
checkHunger()

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
