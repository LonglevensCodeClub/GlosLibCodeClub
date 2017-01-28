from random import randint

def colstick(booksize):
	stickbuy = 0
	stick = dict()
	
	while not (len(stick) == booksize):
		stickbuy += 1
		s = randint(1,booksize)
		if s in stick:
			stick[s] += 1
		else:
			stick[s] = 1
	return stickbuy

y = input("enter book size: ")
x = colstick(int(y))
print ("{} stickers needed to fill a collection of {} ".format(x, y))
z = x - int(y)
print ("with " + str(z) + " swaps")
