from turtle import *
from random import *
speed(0)
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
	penup()
	x = randint(-400, 400)
	y = randint(-1000, 1000)
	goto(x, y)
	pendown()
shape("turtle")

def randomheading():
	setheading(randint(1,360))
	
randomheading()

clear()
setheading(0)

def drawrectangle():
	randomcolor()
	randomplace()
	hideturtle()
	lenght = randint(10,100)
	height = randint(10,100)
	begin_fill()
	forward(lenght)
	right(90)
	forward(height)
	right(90)
	forward(lenght)
	right(90)
	forward(lenght)
	right(90)
	end_fill()

while True:
	drawrectangle()

done()

