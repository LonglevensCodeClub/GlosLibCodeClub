
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
turtlesize(1)

#for i in range(1, 30):
#	randomcolor()
#	randomplace()
#	randomheading()
#	stamp()

shape ("turtle")
speed(0)

# This is a function to draw rectangles
def drawrectangle():
	randomcolor()
	randomplace()
	hideturtle()
	length=randint(10,100)  
	height=randint(10,100)
	begin_fill()
	forward(length)
	right((90)
	forward(height)
	right(90)

	
	
	

done() # always\ at end

