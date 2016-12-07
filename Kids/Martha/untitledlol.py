
from turtle import *
from random import randint

w = Screen()

myTurtle1=Turtle()
myTurtle2=Turtle()
myTurtle3=Turtle()

pensize(3)
speed(10000)
shape('turtle')
color('red')

def updateFrame(step):
	left(12)
	color('orange')
	forward(step)
	color('yellow')
	right(21)
	color('green')
	back(37)
	color('blue')
	left(39)
	color('purple')
	forward(7)
	color('pink')
	color('red')
	right(85)
	color('brown')
	back(55)
	color('black')
	return step+1

def rightArrow():
	pensize(13)
w.onkey(rightArrow, "Right")
	
def leftArrow():
	color('pink')
w.onkey(leftArrow, "Left")
	
def upArrow():
	pensize(6)
w.onkey(upArrow, "Up")
	
def downArrow():
	pensize(1)
w.onkey(downArrow, "Down")

def spacebar():
	color('purple')
w.onkey(spacebar, "space")

#def shift():
#	size(6)
#w.onkey(shift, "shrink")

## Stay at end
w.listen()

while True:
	step = 63
	step = updateFrame(step)
	w.getcanvas().update_idletasks()
	w.getcanvas().update()
