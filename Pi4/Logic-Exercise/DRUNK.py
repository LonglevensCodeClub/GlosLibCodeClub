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
	drunk = askQuestion("are you drunk?")

	print("drunk: " + str(drunk))

	if (not drunk):
		# Can you go to the museum ? Print a message to tell you the answer.
		print("i am glad that you are not drunk.")
	else:
		# Can you go to the museum ? Print a message to tell you the answer.
		print("hello drunk person.")
		
		
checkMusuemVisit

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
