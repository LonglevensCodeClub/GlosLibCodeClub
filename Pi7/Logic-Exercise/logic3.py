#!/usr/bin/env python3
#########################################################
#
# Logic Programming - NOT
#
#########################################################
from logicUtils import *

##########
#
# Here we have defined a function for checking if we can visit the museum
# this function is then called below
#
##########
def checkMuseumVisit():
	weekday = askQuestion("Is it a weekday?")

	print("Weekday: " + str(weekday))

	if (not weekday):
		# Can you go to the museum ? Print a message to tell you the answer.
		print("You can go to the museum.")
	else:
		# Can you go to the museum ? Print a message to tell you the answer.
		print("You can't go to the museum.")

## You can comment this out when you just want to run your own questions below
checkMuseumVisit()

##########
#
# Exercise: Write another question that asks
#	* 'have you seen a rainbow today'
# If they have NOT seen a rainbow, then suggest
#	* 'watch out for sun and rain, then get outside!'
# otherwise print out
#	* 'rainbows are awesome'
#
##########
