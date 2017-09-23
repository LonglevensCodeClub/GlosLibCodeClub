from StarWarsStickersCollectionForOneTurtle import *
import turtle
import random

#function to create a new turtle
def createTurtle():
    #create the turtle
    c = turtle.Turtle()
    c.shape("square")
    c.penup()
    c.speed(100)
    
    #put the turtle in the right place
    x = randint(-400, 400)
    y = randint(-400, 400)
    c.setposition(x, y)
    
    return c
    
stickerTurtles = dict()

# our new observer
def observer(whichSticker, count):
    print("observed sticker {} is at {}".format(whichSticker, count))
    
    #get the turtle from our dictionary, or create a new one
    if whichSticker in stickerTurtles:
        stickerTurtle = stickerTurtles[whichSticker]
    else:
        stickerTurtle = createTurtle()
        stickerTurtles[whichSticker] = stickerTurtle

myBookSize = 324
stickersBought = collectStickers(myBookSize, observer)
print("Bought {} stickers for a collection of {}".format(stickersBought, myBookSize))

#loops = 1
#total = 0.
#totall = 0.
#for i in range(loops):
#	x = collectStickers(myBookSize)
#	y = x / 2
#	totall += y
#	total += x
	#print("bought {} packs for a collection of {}" .format(x, myBookSize))

#average = total / loops
#priceAverage = totall / loops
#print("\n\nThis is a star wars sticker collection.\n")
#print("1 person is collecting the stickers and there are {} stickers in the collecion.\n".format(myBookSize))
#print("There are 5 stickers per pack and each pack costs 50p.\n")
#print("Average amount of packs bought: {}".format(average))
#print("Average amount spent on sticker/packs: {} pounds\n".format(priceAverage)) 
#print("Now we can send in for the last 25 stickers to complete our collection!")

createTurtle()
turtle.done()
