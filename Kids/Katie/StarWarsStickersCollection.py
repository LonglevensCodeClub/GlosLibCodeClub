
from random import randint

def CollectStickers(bookSize):
	stickersBought = 0
	stickers = dict() 
	packsbought = 0
	while not (len(stickers) >= bookSize - 25):

		packSize = 5

		packsbought = packsbought + 1
		for a in range(packSize):
			stickersBought = stickersBought + 1
			s = randint(1, bookSize)
			if s in stickers:
				stickers[s] += 1
			else:
				stickers[s] = 1

	mostSwaps = 0
	stickerSwap = 0
	for s in stickers.keys():
		if (stickers[s] > mostSwaps):
			mostSwaps = stickers[s]
			stickerSwap = s
	print("Most swaps are {} for sticker {}.".format(mostSwaps, stickerSwap))
		
	return packsbought

myBookSize = 324

loops = 20
total = 0
totall = 0
for i in range(loops):
	x = CollectStickers(myBookSize)
	y = x / 2
	totall += y
	total += x
	print("bought {} packs for a collection of {}" .format(x, myBookSize))

average = total / loops
priceAverage = totall / loops
print("Average amont of packs you have to by to complete colection: {}".format(average))
print("Average amont spent on sticker/packs: {} pounds".format(priceAverage))
