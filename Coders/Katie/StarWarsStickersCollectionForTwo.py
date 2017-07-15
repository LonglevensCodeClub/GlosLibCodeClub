
from random import randint

def CollectStickers(bookSize):
	stickersBought = 0
	stickers = dict() 
	stickers2 = dict()
	packsbought = 0
	while not (len(stickers) >= bookSize - 25 and len(stickers2) >= bookSize - 25):

		packSize = 5

		packsbought = packsbought + 1
		for a in range(packSize):
			stickersBought = stickersBought + 1
			s = randint(1, bookSize)
			if s in stickers:
				if s in stickers2:
					stickers[s] += 1
				else:
					stickers2[s] = 1
			else:
				stickers[s] = 1


		packsbought = packsbought + 1
		for a in range(packSize):
			stickersBought = stickersBought + 1
			s = randint(1, bookSize)
			if s in stickers2:
				if s in stickers:
					stickers2[s] += 1
				else:
					stickers[s] = 1
			else:
				stickers2[s] = 1

	mostSwaps = 0
	stickerSwap = 0
	for s in stickers.keys():
		if (stickers[s] > mostSwaps):
			mostSwaps = stickers[s]
			stickerSwap = s
	#print("Most swaps are {} for sticker {}.".format(mostSwaps, stickerSwap))
		
	return packsbought

myBookSize = 324

loops = 10
total = 0
totalPrice = 0
for i in range(loops):
	packsYouBought = CollectStickers(myBookSize)
	moneyYouSpent = packsYouBought / 2.
	totalPrice += moneyYouSpent
	total += packsYouBought
	#print("bought {} packs for a collection of {}" .format(x, myBookSize))

average = total / loops
priceAverage = totalPrice / loops
individualPriceAverage = priceAverage / 2. 
print("this is a star wars sticker collection\n")
print("each pack costs 50 pence and each pack has 5 stickers in it and the whole collection is 324 stickers big\n")
print("Average amount of packs you have to buy to complete two colections: {}".format(average))
print("Average amount spent on sticker/packs: {} pounds".format(priceAverage))
print("Average amount spent by one person: {}".format(individualPriceAverage)) 
