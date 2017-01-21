#bbbbbbbbbbbbbbbbbbbbbbllllllllllllllllaaaaaaaaaaaahhhhhhhhhhhh bbbbbbbbbbbllllllaaaaaaah bbbbbbbbbblllllllaaaaaaaaahh
from random import randint

def collectStickers(bookSize):
	stickersBought = 0
	stickers = dict()
	while not (len(stickers) == bookSize):
		stickersBought = stickersBought + 1
		s = randint(1, bookSize)
		if s in stickers:
			stickers[s] += 1
		else:
			stickers[s] = 1
		
	
	return stickersBought
#10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 poops
x = collectStickers(10)
print("Bought {} packs for a  collection of 100 stickers".format(x))





