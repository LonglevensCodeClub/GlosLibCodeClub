from turtle import *
from random import randint

speed(0)
penup()
goto(-140, 140)

for step in range(24):
 write(step, align='center')
 right(90)
 forward(150)
 pendown()
 forward(10)
 penup()
 backward(160)
 left(90)
 forward(20)

ada = Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-160, 100)
ada.pendown()

for turn in range(100):
 ada.forward(randint(1,5))
bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160, 70)
bob.pendown()

for turn in range(100):
 ada.forward(randint(1,5))
 bob.forward(randint(1,5))


