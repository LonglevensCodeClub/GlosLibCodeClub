from turtle import *
from random import *

colormode(255)

speed (0)
turtlesize(5)

def randomplace():
	red = randint(0, 255)
	green = randint(0, 255)
	blue  = randint(0,255)
	color(red, green, blue)

def randomcolour():
	penup()
	x = randint(-400, 300)
	y = randint(-300, 400)
	goto(x, y)
	pendown()
	
shape("turtle")

while True:
    randomcolour()
    randomplace()
    
    stamp()

done() # leave at end
