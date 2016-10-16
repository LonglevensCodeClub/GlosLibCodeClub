
from turtle import *
from random import randint

myTurtle1=Turtle()
myTurtle2=Turtle()
myTurtle3=Turtle()


pensize(3)
speed(10000)
shape('turtle')
step=63
color('red')
for x in range(100):
	while True:
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
		right(85)
		color('brown')
		back(55)
		color('black')
		step=step+1
	
done()
