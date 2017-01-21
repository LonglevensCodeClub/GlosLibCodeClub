from random import randint

def CollectStickers(bookSize):
	stickersBought = 0
	stickers = dict() 
    
	while not (len(stickers) == bookSize - 20):
		stickersBought += 1
		s = randint(1, bookSize)
		if s in stickers:
			stickers[s] += 1
		else:
			stickers[s] = 1
		
	return stickersBought

myBookSize = 320

loops = 20
total = 0
for i in range(loops):
	x = CollectStickers(myBookSize)
	total += x
	print("bought {} stickers for a collection of {}" .format(x, myBookSize))

average = total / loops
print("Average of {} stickers required".format(average))
print("Average of {} stickers required".format(average))
