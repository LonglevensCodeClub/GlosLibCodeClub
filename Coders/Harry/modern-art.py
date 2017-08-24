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
	x = randint(-1, 1)
	y = randint(-1, 1)
	goto(x, y)
	pendown()
	
def randomheading():
	setheading(randint (1, 360))
	
shape("turtle")
turtlesize(1)

#while True:
	#randomcolor()
	#randomplace()
	#randomheading()
	#stamp()
	
def drawrectangle():
   randomcolor()
   randomplace()
   hideturtle()
   length = randint(10, 100)
   height = randint(10, 100)
   begin_fill()
   forward(length)
   right(90) 
   forward(height)
   right(90)
   forward(length)
   right(90)
   forward(height)
   right(90)
   end_fill()
clear()
setheading(0)

def drawcircle():
	length = randint(10, 100)
	randomcolor()
	randomplace()
	dot(length) 

#for i in range(20):
#	drawcircle()
	
def draw_randomshape(size, color):
	randomcolor()
	randomplace()
	angle = 120
	begin_fill()

	for side in range(5):
		forward(size)
		right(angle)
		forward(size)
		right(72 - angle)
	end_fill()
	return

for i in range(50):
	draw_randomshape(100, "purple")
   
done() # holds the screen at end
