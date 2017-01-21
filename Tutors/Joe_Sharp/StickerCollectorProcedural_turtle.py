from StickerCollectorProcedural import *
import turtle
import random
import time
import math

stickerTurtles = []

def observer(whichSticker, count):
	print("Sticker: {}, Count: {}".format(whichSticker, count))
	thisColour = "black" if count == 0 else "green"
	stickerTurtle = stickerTurtles[whichSticker-1]
	stickerTurtle.color(thisColour)
	stickerTurtle.turtlesize(stretch_wid=1 + count)
	
myBookSize = 64
wallDim = math.floor(math.sqrt(myBookSize))
spaceToFill=600
halfSpaceToFill = spaceToFill / 2
spacing = spaceToFill / wallDim

for i in range(1, myBookSize+1):
	c = turtle.Turtle()
	c.shape("turtle")
	c.penup()
	tx = math.floor((i-1) % wallDim)
	ty = math.floor((i-1) / wallDim)
	c.setposition(tx * spacing - halfSpaceToFill, ty * spacing - halfSpaceToFill)
	stickerTurtles.append(c)
	observer(i, 0)

stickers, stickersBought = collectStickers(bookSize=myBookSize, observer=observer)
print("Bought {} stickers for a collection of {}".format(stickersBought, myBookSize))
print("Collection Looks Like This: {}".format(stickers))

turtle.done()
