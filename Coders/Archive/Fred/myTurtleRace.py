from turtle import *
from random import randint

speed(0)
penup()
goto(-140, 140)

for step in range(15):
	write(step, align='center')
	right(90)
	forward(10)
	pendown()
	forward(150)
	penup()
	backward(160)
	left(90)
	forward(20)

red = Turtle()
red.color('red')
red.shape('turtle')

red.penup()
red.goto(-160, 100)
red.pendown()

for turn in range(100):
   red.forward(randint(1,5))
        
blue.= Turtle()
blue.color('blue')
blue.shape('turtle')

blue.penup()
blue.goto(-160, 100)
blue.pendown()

for turn in range(100):
   blue.forward(randint(1,5))

done()
 


