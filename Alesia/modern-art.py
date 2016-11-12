
from turtle import*
from random import*

colormode(255) #always at start

speed(-999999999999999999999999999999999999999999999999999999999)

def randomcolor():
	red=randint(0,255)
	green=randint(0,255)
	blue=randint(0,255)
	color(red,green,blue)

def randomplace():
	penup()
	x = randint(-300, 300)
	y = randint(-300, 300)
	goto(x, y)
	pendown()
	
def randomheading():
	setheading(randint(1, 360))
	
shape("turtle")
turtlesize(15)

while True:
	randomcolor()
	randomplace()
	randomheading()
	stamp()
	randomcolor()
	randomplace()
	randomheading()
	stamp()

done() # always at end

