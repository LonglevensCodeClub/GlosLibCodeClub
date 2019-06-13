from turtle import *
from random import *

shape("turtle")
colormode(255)
speed(0)

def randomcolour():
	red=randint(0, 255)
	green=randint(0, 255)
	blue=randint(0, 255)
	color(red, green, blue)

def randomplace():
	penup()
	x = randint(-100, 100)
	y = randint(-100, 100)
	goto(x, y)
	pendown()
	
def randomheading():
	h = randint(1, 360)
	setheading(h);

def randomall():
	randomcolour()
	randomplace()
	randomheading()

def drawcircle():
	randomall()
	r = randint(5, 150)
	dot(r)

def drawstar():
	randomall()
	begin_fill()
	angle = 120
	size = randint(10, 150)
	for side in range(5):
		forward(size)
		right(angle)
		forward(size)
		right(72 - angle)
	end_fill()

def drawrectangle():
	randomall()
	hideturtle()
	length = randint(10, 100)
	height = randint(10, 100)
	begin_fill()
	for i in range(4):
		forward(length)
		right(90)
	end_fill()
	
def drawshape():
	shape_functions = [drawcircle, drawstar, drawrectangle]
	which = choice(shape_functions)
	which()
	
for i in range(30):
	drawshape()

done()
