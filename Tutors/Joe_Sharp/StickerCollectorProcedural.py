from random import randint

def collectStickers(bookSize, observer=None):
	stickersBought = 0
	stickers = dict()
	
	# Tell the observer about the existence of all stickers
	if observer:
		for x in range(1, bookSize):
			observer(x, 0)
			
	while not (len(stickers) == bookSize):
		stickersBought += 1
		s = randint(1, bookSize)
		if s in stickers:
			stickers[s] += 1
		else:
			stickers[s] = 1
			
		# Update the observer
		if observer:
			observer(s, stickers[s])
	
	return stickersBought
