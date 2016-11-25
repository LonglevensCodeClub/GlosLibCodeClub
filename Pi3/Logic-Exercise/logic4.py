#!/usr/bin/env python3
#########################################################
#
# Logic Programming - Exclusive OR
#
#########################################################
from operator import xor
from logicUtils import *

##########
#
# Here we have defined a function for checking if we are likely to be too hot/cold
# this function is then called below
#
##########
def checkTemperature():
	sunny = askQuestion("Is it sunny?")
	haveCoat = askQuestion("Do you have a coat with you?")

	print("Sunny: " + str(sunny))
	print("You have a coat: " + str(haveCoat))

	if (xor(sunny, haveCoat)):
		# Can you go outside ? Print a message to tell you the answer.
		print("You can go outside")
	elif (sunny and haveCoat):
		# Are you going to be too hot, or too cold ? Print a message to warn you.
		print("You are going to be too hot")
	else:
		# Are you going to be too hot, or too cold ? Print a message to warn you.
		print("You are going to be too cold")

## You can comment this out when you just want to run your own questions below
checkTemperature()

##########
#
# Exercise: Ask the following questions
#	* 'are you travelling on a plane'
#	* 'are you travelling on a boat'
#
# If the person YES to one of the questions, print
#	* 'enjoy your journey'
# Else if they are on a boat AND a plain
#	* 'You can't be on both!'
# otherwise print
#	* 'have a nice day'
#
##########
