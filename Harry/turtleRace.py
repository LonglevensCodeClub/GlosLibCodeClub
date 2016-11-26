from turtle import *
from random import randint
speed(10)
penup()
goto(-140, 140)

for step in range(6):
	write(step, align='center')
	right(90)
	forward(10)
	pendown()
	forward(150)
	penup()
	backward(160)
	left(90)
	forward(20)

myColors=['yellow','pink', 'blue','grey','red','green','midnight blue']
cheater = 'pink'
startPos = 80
myTurtles = []

for c in myColors:
	myTurtle = Turtle()
	myTurtle.color(c)
	myTurtle.shape('turtle')

	myTurtle.penup()
	myTurtle.goto(-160, startPos)
	startPos += 20
	myTurtle.pendown()
	myTurtles.append(myTurtle)
	
for turn in range(100):
	for x in range(len(myTurtles)):
		t = myTurtles[x]
		if myColors[x] == cheater:
			t.forward(5)
		
		t.forward(randint(1,5))
		
	#for t in myTurtles:		
	#	t.forward(randint(1,5))
	
while(True):
	pass

