from turtle import *
from random import randint

speed(20)
penup()
goto(-140, 140)
	
for step in range(10):
	write(step, align = 'center')
	right(90)
	forward(10)
	pendown()
	forward(150)
	penup()
	backward(160)
	left(90)
	forward(20)

myTurtles = ['red', 'green', 'blue', 'yellow', 'purple']

myTs = []

startPos = 100
for myTurtle in myTurtles:
	t = Turtle()
	t.color(myTurtle)
	t.shape('turtle')
	t.penup()
	t.goto(-160, startPos)
	t.pendown()
	startPos -= 25
	myTs.append(t)

for turn in range(100):
	for t in myTs:
		t.forward(randint(1, 5))
	
while(True):
	pass
