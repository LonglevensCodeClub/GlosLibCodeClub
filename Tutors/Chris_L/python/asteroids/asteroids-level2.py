from turtle import *
import random
import math

t = Turtle()
t.ht()
t.penup()


s = Turtle()
s.shape('turtle')
s.color('white')


screenMinX = -t.screen.window_width()/2
screenMinY = -t.screen.window_height()/2
screenMaxX = t.screen.window_width()/2
screenMaxY = t.screen.window_height()/2

t.screen.setworldcoordinates(screenMinX,screenMinY,screenMaxX,screenMaxY)

t.screen.register_shape("ship",((-10,-10),(0,-5),(10,-10),(0,10)))
t.shape("ship")

#t.screen.bgcolor("black")
t.color('red')

s.goto(10,10)


# Setup Screen

def turnLeft():
    t.left(10)

def turnRight():
    t.right(10)

def forward():
    t.penup()
    t.fd(10)

#t.screen.tracer(0);

t.screen.onkey(turnLeft, 'Left')
t.screen.onkey(turnRight, 'Right')
t.screen.onkey(forward, 'Up')

t.screen.listen()

t.screen.exitonclick()