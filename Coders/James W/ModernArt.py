#!/bin/python3

from turtle import *
from random import *

def randomcolour():
 red = randint (0, 255)
 green = randint (0, 255)
 blue = randint (0, 255)
 color(red, green, blue)
 
def randomplace():
  penup()
  x = randint(-100, 100)
  y = randint (-100, 100)
  goto(x, y)
  pendown()

shape("turtle")

#for i in range(30):
#randomcolour()
#randomplace()
#randomheading()
#stamp()

def drawrectangle()
hideturtle()
length = randint(10, 100)
