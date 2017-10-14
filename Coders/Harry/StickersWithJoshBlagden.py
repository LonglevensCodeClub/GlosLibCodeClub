
from random import randint


def collectStickers(bookSize):
	stickersBought = 0
	stickers = dict()
	
	
	while not (len(stickers) == bookSize):
		stickersBought += 1
		s = randint(1, bookSize)
		if s in stickers:
			stickers[s] +=1
		else:
				stickers[s] = 1
				
	return stickersBought

avg =0
loops= 10000

for x in range(loops):
	myBookSize = 10000
	x = collectStickers(myBookSize)
	avg = avg +x
	print("Bought {} stickers for a collection of {}" .format(x, myBookSize))

avg = avg/loops

print("Bought average of {} stickers for a collection of {}" .format(avg, myBookSize))

# Example of loops and strings
#names = ["Harry", "Luke"]
#for name in names:
#	print("Hello {}".format(name))
