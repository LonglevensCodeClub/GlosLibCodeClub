#!/bin/python3

from turtle import *
from random import randint 

penup()
goto(-140,140)
for step in range (15):
    write(step, align='center')
    right(90)
    forward(10)
    pendown ()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)
speed(10)
penup()
goto(-140,140)
forward(20)
ada = Turtle()
ada.color('red')
ada.shape('turtle')#
ada.penup()
ada.goto(-160,100)
ada.pendown()
ada.penup()
ada.goto(-160,100)
ada.pendown()
bob=Turtle()
bob.color('blue')
bob.shape('turtle')
bob.penup()
bob.goto(-160,70)
bob.pendown()
amy=Turtle()
amy.color('pink')
amy.shape('turtle')
amy.penup()
amy.goto(-160,40)
amy.pendown()
kev=Turtle()
kev.color('yellow')
kev.shape('turtle')
kev.penup()
kev.goto(-160,10)
kev.pendown()
for turn in range(100):
    ada.forward(randint(1,5))
    bob.forward(randint(1,5))
    amy.forward(randint(1,5))
    kev.forward(randint(1,5))

    
    



    
    

