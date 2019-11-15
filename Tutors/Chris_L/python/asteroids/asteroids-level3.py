from turtle import *
import random
import math

screen = Screen()

screen.register_shape("ship",((-10,-10),(0,-5),(10,-10),(0,10)))
screen.bgcolor("black")

screenMinX = -screen.window_width()/2
screenMinY = -screen.window_height()/2
screenMaxX = screen.window_width()/2
screenMaxY = screen.window_height()/2

screen.setworldcoordinates(screenMinX,screenMinY,screenMaxX,screenMaxY)


class SpaceShip(Turtle, x , y):
    def __init__(self):
        Turtle.__init__(self)

        self.shape("ship")
        self.color('red')

ship = SpaceShip(10,10)



def turnLeft():
    ship.left(10)

def turnRight():
    ship.right(10)

def forward():
    ship.penup()
    ship.fd(10)


screen.onkey(turnLeft, 'Left')
screen.onkey(turnRight, 'Right')
screen.onkey(forward, 'Up')

screen.listen()

screen.exitonclick()