#!/usr/bin/python3
from random import randint

def colstick(booksize, observer=None):
	stickbuy = 0
	stick = dict()
	if observer:
                for a in range (1, booksize):
                        observer(a, 0)
	
	while not (len(stick) == booksize):
		stickbuy += 1
		s = randint(1,booksize)
		if s in stick:
			stick[s] += 1
		else:
			stick[s] = 1
		if observer:
                        observer(s, stick[s])
	return stickbuy
