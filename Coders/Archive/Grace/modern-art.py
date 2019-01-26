from turtle import *
from random import *

colormode(255)

speed (0)
turtlesize(2.3)

def randomplace():
	red = randint(0, 255)
	green = randint(0, 255)
	blue  = randint(0,255)
	color(red, green, blue)

def randomcolour():
	penup()
	x = randint(-200, 200)
	y = randint(-200, 200)
	goto(x, y)
	pendown()
	
shape("turtle")

#for i in range(1,30):
#    randomcolour()
#    randomplace()   
#	 randomheading() 
#    stamp()

def drawcircle():
	randomcolour()
	randomplace()
	hideturtle()
	length = randint(10,100)
	height = randint(10,100)
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
	
def star():
    randomcolour()
    randomplace()
    begin_fill()
    side = randint(10, 50)
    for i in range(5):
        forward(side)
        right(144)
        forward(side)
    end_fill()

while True:
	star()

done()  #leave at end
