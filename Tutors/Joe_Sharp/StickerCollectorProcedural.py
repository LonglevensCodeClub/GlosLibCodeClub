from random import randint

def collectStickers(bookSize):

	stickers = dict()
	stickersBought = 0

	while not (len(stickers) == bookSize):
		stickersBought += 1
		s = randint(1, bookSize)
		if s in stickers:
			stickers[s] += 1
		else:
			stickers[s] = 1

	return stickersBought

attempts=100
myBookSize=400
totalStickers=0

for x in range(attempts):
	b = collectStickers(bookSize=400)
	print("Bought {} stickers to collect {}".format(b, myBookSize))
	totalStickers+=b

average = totalStickers / attempts

print("Bought an average of {} stickers to collect {} in {} attempts".format(average, myBookSize, attempts))

