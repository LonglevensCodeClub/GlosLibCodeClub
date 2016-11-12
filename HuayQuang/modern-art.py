from turtle import *
from random import *
                      # space needed
colormode(255) # always at start
# space needed
def randomcolor():
	red = randint(0, 255) #color
	green = randint(0, 255) #color
	blue = randint(0,255)
	color(red, green, blue)
	#space needed
def randomplace():
	pendown()
	x = randint(-100, 100)
	y = randint(-100, 100)
	goto(x, y)
	penup()
shape("turtle") # shape
randomcolor()
randomplace()
stamp() 
randomcolor()
randomplace()
stamp()
randomcolor()
# space needed
done()           # always at end, holds the screen in place
