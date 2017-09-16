from StarWarsStickersCollectionForOneTurtle import *

# our new observer
def observer(whichSticker, count):
    print("observed sticker {} is at {}".format(whichSticker, count))


myBookSize = 324

loops = 20
total = 0.
totall = 0.
for i in range(loops):
	x = CollectStickers(myBookSize)
	y = x / 2
	totall += y
	total += x
	#print("bought {} packs for a collection of {}" .format(x, myBookSize))

average = total / loops
priceAverage = totall / loops
print("\n\nThis is a star wars sticker collection.\n")
print("1 person is collecting the stickers and there are {} stickers in the collecion.\n".format(myBookSize))
print("There are 5 stickers per pack and each pack costs 50p.\n")
print("Average amount of packs bought: {}".format(average))
print("Average amount spent on sticker/packs: {} pounds\n".format(priceAverage)) 
print("Now we can send in for the last 25 stickers to complete our collection!")


