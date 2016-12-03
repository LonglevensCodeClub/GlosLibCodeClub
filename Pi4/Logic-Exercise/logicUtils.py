#!/usr/bin/env python3
#########################################################
#
# Logic Programming
#
#########################################################

def strToBoolean(s):
   return s.lower() in ('y')
   
def askQuestion(s):
	return strToBoolean(input("%s [Y|N]: " % s))
