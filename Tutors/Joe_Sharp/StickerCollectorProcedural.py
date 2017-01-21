from random import randint

def collectStickers(bookSize, observer=None):
	stickersBought = 0
	stickers = dict()
	
	while not (len(stickers) == bookSize):
		stickersBought += 1
		s = randint(1, bookSize)
		if s in stickers:
			stickers[s] += 1
		else:
			stickers[s] = 1
		if observer:
			observer(s, stickers[s])
	
	return stickers, stickersBought
	


