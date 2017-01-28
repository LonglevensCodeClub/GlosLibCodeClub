from StickerCollectorProcedural import *
import turtle
import random

turtle.setup(width=800, height=800)

# Function to create a new turtle
def createTurtle():	
	# Create the turtle
	c = turtle.Turtle()
	c.shape("square")
	c.penup()
	c.speed(100)
	
	# Put the turtle in the right place
	x = randint(-400, 400)
	y = randint(-400, 400)
	c.setposition(x, y)
	
	return c
	
stickerTurtles = dict()

# Our new observer
def observer(whichSticker, count):
	print("Observed sticker {} is at {}".format(whichSticker, count))
	
	# Get the turtle from our dictionary, or create a new one
	if whichSticker in stickerTurtles:
		stickerTurtle = stickerTurtles[whichSticker]
	else:
		stickerTurtle = createTurtle()
		stickerTurtles[whichSticker] = stickerTurtle
		
	# Update the state of the turtle depending on the count
	thisColour = "red" if count == 0 else "green"
	thisSize = 1 + (count / 3)
	
	stickerTurtle.color(thisColour)
	stickerTurtle.turtlesize(thisSize)
		
bookSize=20
stickersBought = collectStickers(bookSize, observer)
print("Bought {} stickers for a collection of {}".format(stickersBought, bookSize))

turtle.done()
