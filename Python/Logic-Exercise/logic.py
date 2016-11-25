#!/usr/bin/env python3
#########################################################
#
# Logic Programming
#
#########################################################
from operator import xor

def strToBoolean(s):
   return s.lower() in ('t', 'y')

weekday = strToBoolean(input("Is it a weekday [Y|N] ?"))
termtime = strToBoolean(input("Is it school term time [Y|N] ?"))
sunny = strToBoolean(input("Is it sunny [Y|N] ?"))
haveCoat = strToBoolean(input("Do you have a coat with you [Y|N] ?"))

print("Weekday: " + str(weekday))
print("Term-time: " + str(termtime))
print("Sunny: " + str(sunny))
print("You have a coat: " + str(haveCoat))

if (weekday and termtime):
    # Should you be going to school ? Print a message to tell you the answer.
    print("It's a school day!")
else:
    # Should you be going to school ? Print a message to tell you the answer.
    print("It's not a school day!")

if (not weekday):
    # Can you go to the park ? Print a message to tell you the answer.
    print("You can go to the park.")
else:
    # Can you go to the park ? Print a message to tell you the answer.
    print("You can't go to the park.")

if (xor(sunny, haveCoat)):
    # Can you go outside ? Print a message to tell you the answer.
    print("You can go outside")
elif (sunny and haveCoat):
    # Are you going to be too hot, or too cold ? Print a message to warn you.
    print("You are going to be too hot")
else:
    # Are you going to be too hot, or too cold ? Print a message to warn you.
    print("You are going to be too cold")

