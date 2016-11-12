from turtle import *
from random import *

colormode(255) # leave at start

speed(0)

def randomcolor():
	red = randint(0, 225)
	green = randint(0, 225)
	blue = randint(0, 225)
	color(red, green, blue)

def randomplace():
	penup()
	x = randint(-200, 200)
	y = randint(-100, 100)
	goto(x, y)
	pendown()
	
def randomheading():
	setheading(randint (1, 360))
	
shape("turtle")
turtlesize(9)

while True:
	randomcolor()
	randomplace()
	randomheading()
	stamp()

done() # holds the screen at end
