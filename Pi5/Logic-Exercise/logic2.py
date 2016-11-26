#!/usr/bin/env python3
#########################################################
#
# Logic Programming - AND
#
#########################################################
from logicUtils import *

##########
#
# Here we have defined a function for checking if it's a school day
# this function is then called below
#
##########
def checkSchoolDay():
	weekday = askQuestion("Is it a weekday?")
	termtime = askQuestion("Is it school term time?")

	print("Weekday: " + str(weekday))
	print("Term-time: " + str(termtime))

	if (weekday and termtime):
		# Should you be going to school ? Print a message to tell you the answer.
		print("It's a school day!")
	else:
		# Should you be going to school ? Print a message to tell you the answer.
		print("It's not a school day!")
		
## You can comment this out when you just want to run your own questions below
#checkSchoolDay()

##########
#
# Exercise: Write two more questions:
#	* 'do you have a dog'
#   * 'have you been outside today'
# Then process the answers as suggested
#
# If the answer to both is yes then suggest
#	* 'take the dog for a walk'
# If you don't have a dog, but haven't been outside yet then suggest
#	* 'it would be nice to go for a walk'
# otherwise print out
#	* 'i'm glad you have had some fresh air'
#
##########

def checkifwearingbra():
	woman = askQuestion("Are you a woman?")
	bra = askQuestion("Are you wearing a bra?")
     
	print("Woman: " + str(woman))
	print("bra: " + str(bra))
    
	if (woman and bra):
		print("Your a woman with a bra!")
	else:
		print("Your not a woman with a bra?Thats illegal!")
		
checkifwearingbra()
