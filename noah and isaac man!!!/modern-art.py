from turtle import*
from random import*

colormode(255) # leave at start

def randomcolour():
	red=randint(0, 225)
	green=randint(0,255)
	blue=randint(0,255)
	color(red,green,blue)

shape ("turtle")
randomcolour()

def randomplace():
	penup()
	x = randint(-100,100)
	y = randint(-100,100)
	goto(x,y)
	pendown()

def randomheading():
	setheading(randint(1, 360))

shape("turtle")
speed(0)
for i  in range(30):
	randomcolour()
	randomplace()
	randomheading()
	stamp()

#def drawrectangle():
#	randomcolour()
	#randomplace()-
	#hideturtle()
	#length = randint(10, 100)
	#height = randint(10, 100)
	#begin_fill()
	#forward(length)
	#right(90)
	#forward(height)
	#right(90)
	#forward(length)
	#right(90)
	#forward(height)
	#right(90)
	#end_fill()
	
clear()
setheading(0)

#for i in range(0):
while True:
	drawrectangle()
	
	done() 
