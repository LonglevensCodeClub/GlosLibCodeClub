#!/bin/python3

from turtle import *
from random import *

colormode(255)

def randomColour():
   red   = randint(0,255)
   green = randint(0,255)
   blue  = randint(0,255)
   color(red, green, blue)


def randomPlace():
   penup()
   x = randint(-100, 100)
   y = randint(-100, 100)
   goto(x, y)
   pendown()

def randomHeading():
   setheading(randint(1, 360))

def drawRectangle():
   randomColour()
   randomPlace()
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


   
shape("turtle")
speed(0)

randomColour()
randomPlace()
randomHeading()
stamp()

clear()
setheading(0)

for i in range(1, 30):
   randomColour()
   randomPlace()
   randomHeading()
   stamp()

clear()
setheading(0)

for i in range(20):
   drawRectangle()

clear()

for i in range(20):
   randomColour()
   randomPlace()
   dot(randint(1, 100))   
